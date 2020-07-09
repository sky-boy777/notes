import requests


class TieBa():
	def __init__(self,tieba_name):
		'''接收贴吧名字'''
		self.tieba_name = tieba_name
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
		self.url = "https://tieba.baidu.com/f?kw="+ tieba_name +"&ie=utf-8&pn=%s"

	def get_url_list(self):
		'''创建url列表'''
		#url_list = []
		#for i in range(3):
			#url_list.append(self.url%i*50)
		#return url_list

		#使用列表推导式
		return [self.url%i*50 for i in range(3)]

	def save_html(self,str_html,page_num):
				file_name = "第%s页--%s.html"%(page_num,self.tieba_name)
				with open(file_name,"w",encoding = "utf-8") as f:
					f.write(str_html)

					
	def run(self):
		'''执行函数'''
		#获取url列表
		url_list = self.get_url_list()
		page_num = 1
		
		#循环发送请求并将结果解码
		for url in url_list:
			str_html = requests.get(url,self.headers).content.decode()

                        #保存
			self.save_html(str_html,page_num)
			page_num += 1
			

if __name__ == '__main__':
	tb = TieBa("李毅")
	tb.run()
