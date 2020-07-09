import requests
import json
import pprint


class DouBan():
	'''爬取豆瓣电视数据'''
	def __init__(self):
		self.headers = {"Referer": "https://m.douban.com/tv/american","User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36"}
		self.url = [
			"https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288",
			"https://m.douban.com/rexxar/api/v2/subject_collection/tv_korean/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288",
			"https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288",
			"https://m.douban.com/rexxar/api/v2/subject_collection/tv_japanese/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288",
			"https://m.douban.com/rexxar/api/v2/subject_collection/tv_animation/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288",
			"https://m.douban.com/rexxar/api/v2/subject_collection/tv_variety_show/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288"
					]

	def get_url(self,pag, url):
		'''发送请求获取数据'''
		response = requests.get(url.format(pag), headers = self.headers)
		return response.content.decode()


	def run(self):
		#发送请求获取响应
		for url in self.url:
			print("*"*50)
			pag = 0
			while True:
				json_str = self.get_url(pag, url)
				#print(type(json_str))

				#提取数据
				#python类型的数据
				rep_dict = json.loads(json_str)

				#列表
				rep_list = rep_dict["subject_collection_items"]
				if len(rep_list) <=0:
					break

				#保存数据，只能写入str类型
				with open("douban.txt", "a", encoding="utf-8") as f:
					for content in rep_list:
						json.dump(content, f, ensure_ascii=False)    #ensure_ascii=Fales显示中文内容
						#f.write(json.dumps(content, ensure_ascii=False))
						f.write("\n")

				pag += 18


if __name__ == '__main__':
	douban = DouBan()
	douban.run()
