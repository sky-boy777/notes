# -*- coding: utf-8 -*-
import scrapy
import re

class QqLoginSpider(scrapy.Spider):
    name = 'qq_login'
    allowed_domains = ['qq.com']
    start_urls = ['https://h5.qzone.qq.com/mqzone/profile?hostuin=1251779123&no_topbar=1&srctype=10&stat=&g_f=2000000209']

    def start_requests(self):
        """重写请求方法，使能携带cookies"""
        #使用字典推导式将cookies改为字典形式
        cookies = "pgv_pvi=7059612672; pgv_si=s9676323840; _qpsvr_localtk=0.43995800563443277; ptui_loginuin=1251779123; RK=bliwgN4GYA; ptcz=c701f84c26c2a750934a7116a19a5261496ed535f0aed9667bce8e23c6024d27; pgv_pvid=8857791840; pgv_info=ssid=s5746642326; Loading=Yes; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; uin=o1251779123; skey=@K9eoEtH27; p_uin=o1251779123; cpu_performance_v8=2; pt4_token=rjjQJImfLwabdzVu9s-hqJ2Hw4aIL89F2zo7-XrZEtU_; p_skey=bEpPGlkgW0h6MtUL92ljScDrmsv5tAaocYyD3fJirCQ_"
        # 按分号空格（; ）分割，然后再按等号（=）分割
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}

        #self.start_url是一个列表，不能直接请求，要提取出里面的地址出来_
        yield scrapy.FormRequest(self.start_urls[0], callback=self.parse, cookies=cookies)

    def parse(self, response):
        print(re.findall("糖果聪", response.body.decode()))





