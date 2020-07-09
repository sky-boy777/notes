from selenium import webdriver   # 浏览器
from lxml import etree  # 提取数据
import time  # 请求延迟
import re  # 美化数据
import json  # 保存数据
import random  # 请求随机延迟的时间

'''
爬取拉钩网python职位信息
'''

def main():
    # 使用代理,防止自己电脑IP被封(使用的是免费的代理，所以很不稳定)
    agency = webdriver.ChromeOptions()
    # agency.add_argument("--proxy-server=http://123.169.124.166:9999")

    # 实例化一个浏览器驱动,这里使用谷歌的驱动(注意：chromedriver要跟你电脑上安装的谷歌浏览器版本一致，否则报错)
    g_driver = webdriver.Chrome(options=agency)

    # 最先打开的网址
    start_url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    # 打开网址
    g_driver.get(url=start_url)
    g_driver.find_element_by_xpath('//div[@class="body-btn"]').click()  # 关闭广告弹窗

    while True:
        # 提取所有职位的链接,得到一个url列表
        url_list = g_driver.find_elements_by_xpath('//a[@class="position_link"]//h3')
        for detail_url in url_list:
            #time.sleep(random.randint(2, 5))  # 随机等待几秒

            # 点击链接进入职位详情页（点击后会打开一个新的窗口）
            detail_url.click()
            # 切换到新的窗口
            handle = g_driver.window_handles
            g_driver.switch_to.window(handle[1])

            # 提取详情页的数据
            html = etree.HTML(g_driver.page_source)
            # 信息用字典存储
            item = {}
            # 职位
            item["职位"] = html.xpath('//h1[@class="name"]/text()')[0]
            item["公司"] = [i.strip() for i in html.xpath('//em[@class="fl-cn"]/text()')][0]
            item["发布时间"] = re.sub(r'\xa0', '', html.xpath('//p[@class="publish_time"]/text()')[0])  # 随便用正则替换一下字符

            job_detail = html.xpath('//dd[@class="job_request"]/h3//span/text()')
            job_detail = [i.strip("/") for i in job_detail]  #去掉两边斜杠
            item["工作要求"] = [i.strip() for i in job_detail]  #去掉两边空格

            job_detail = html.xpath('//div[@class="job-detail"]//text()')
            job_detail = [i.strip() for i in job_detail]   #去掉两边空格
            item["岗位详情"] = [i for i in job_detail if len(i) > 0]  # 去掉空字符串
            print(item)

            # 存储到文件
            with open("lagou.json", "a", encoding="utf-8") as f:
                json.dump(item, f, ensure_ascii=False)
                f.write("\n")

            # 关闭当前窗口并且定位到第一个窗口，不然会报错
            g_driver.close()
            g_driver.switch_to.window(handle[0])

        # 点击下一页
        # 先判断是否还有下一页
        if g_driver.find_element_by_xpath('//span[@action="next"]').get_attribute("class") != "pager_next pager_next_disabled":
            g_driver.find_element_by_class_name("pager_next ").click()
            time.sleep(2)  # 等待页面加载
        else:
            break

    # g_driver.close()

if __name__ == '__main__':
    main()