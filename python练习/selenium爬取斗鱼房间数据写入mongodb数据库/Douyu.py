from selenium import webdriver
import time
import json
from pymongo import MongoClient

#连接到douyu数据库
db = MongoClient(host="127.0.0.1", port=27017).douyu

url = "https://www.douyu.com/directory/all"

Gdriver = webdriver.Chrome()

# 发送请求
Gdriver.get(url)

#打开浏览器后等待几秒，让页面加载完成
time.sleep(3)

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

        #将数据写入数据库
        db.aa.insert_one(room_dict)





    # 请求下一页地址，循环
    next_page = Gdriver.find_element_by_xpath("//li[@class=' dy-Pagination-next']/span")
    next_page.click()  #点击下一页
    time.sleep(3)  #睡眠3秒

#退出浏览器
Gdriver.quit()

