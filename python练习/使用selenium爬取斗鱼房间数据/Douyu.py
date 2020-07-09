from selenium import webdriver
import time
import json

url = "https://www.douyu.com/directory/all"

Gdriver = webdriver.Chrome()

# 发送请求
Gdriver.get(url)

#打开浏览器后等待几秒，让页面加载完成
time.sleep(2)

next_page = True
while next_page is not None:
    # 提取数据
    room_list = Gdriver.find_elements_by_xpath("//li[@class = 'layout-Cover-item']")
    content_list = []   #一个存放字典的列表
    for i in room_list:
        room_dict = {}
        room_dict["标题"] = i.find_element_by_xpath(".//h3[@class='DyListCover-intro']").get_attribute("title")
        room_dict["类型"] = i.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
        room_dict["主播name"] = i.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
        room_dict["热度"] = i.find_element_by_xpath(".//span[@class = 'DyListCover-hot']").text
        print(room_dict)
        content_list.append(room_dict) #将字典数据放入列表

    # 保存数据
    with open("斗鱼.txt", "a", encoding="utf-8") as f:
        for i in content_list:
            print(type(i))
            f.write(json.dumps(i, ensure_ascii=False))
            f.write("\n\n")

    # 请求下一页地址，循环
    next_page = Gdriver.find_element_by_xpath("//li[@class=' dy-Pagination-next']/span")
    next_page.click()  #点击下一页
    time.sleep(3)  #睡眠3秒

#退出浏览器
Gdriver.quit()

