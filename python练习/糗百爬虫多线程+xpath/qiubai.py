import requests
from lxml import etree
import threading
from queue import Queue


class Qiubai:
    def __init__(self):
        self.headers = {
            "sec - fetch - dest": "empty",
            "sec - fetch - mode": "cors",
            "sec - fetch - site": "cross - site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
        self.url_list = Queue()  #url队列
        self.res = Queue()  #响应队列
        self.str = Queue()  #数据队列

    def get_url_list(self):
        '''url队列'''
        url = "https://www.qiushibaike.com/text/page/{}/"
        for i in range(13):
            self.url_list.put(url.format(i))  #循环，创建url队列

    def get_html(self):
        '''发送请求'''
        while True:
            url = self.url_list.get()  #从队列取出
            response = requests.get(url, headers=self.headers)  #发送请求
            self.res.put(response.content.decode())  #放入队列
            self.url_list.task_done()  #让队列减一

    def get_html_data(self):
        '''提取数据'''
        while True:
            html_str = self.res.get()  #取出一个响应

            #提取数据
            html = etree.HTML(html_str)
            content_list = html.xpath('//div[@class="content"]')

            self.str.put(content_list)  #放入队列
            self.res.task_done()  #res让队列减一

    def save_data(self):
        '''保存'''
        while True:
            content_list = self.str.get()  # 从队列取出一个
            with open("糗事百科搞笑段子.text", "a", encoding="utf-8") as f:
                for i in content_list:
                    i = i.xpath("./span/text()")  # 列表
                    for j in i:
                        a = j.replace("\n", "")  # 去掉\n符号
                        f.write(a)
                    f.write("\n\n\n")
            self.str.task_done()  # 队列减一


    def run(self):
        '''创建线程并开启'''
        #一个空列表，将所有线程放入里面，然后用for循环start
        thread_list = []

        #创建url队列
        url = threading.Thread(target=self.get_url_list)
        thread_list.append(url)

        #发送请求
        for i in range(20):
            send = threading.Thread(target=self.get_html)
            thread_list.append(send)

        #提取数据
        for i in range(10):
            get_data = threading.Thread(target=self.get_html_data)
            thread_list.append(get_data)

        #保存数据
        for i in range(20):
            save_data = threading.Thread(target=self.save_data)
            thread_list.append(save_data)

        #开始线程
        print("开始")
        for i in thread_list:
            i.daemon = True  #子线程设置为守护线程，主线程结束子线程结束
            i.start()
        for j in [self.url_list, self.res, self.str]:
            j.join()  #让主线程等待子线程结束再结束

        print("结束")


if __name__ =="__main__":
    qiubai = Qiubai()
    qiubai.run()
