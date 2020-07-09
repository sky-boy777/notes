# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import re


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.homepage1.99345513004.47&safpn=10001']

    def parse(self, response):
        """大类别"""
        div_list = response.xpath("//div[@class='menu-list']/div[@class='menu-item'][position()<9]")

        for i in div_list:
            item = {}
            item["大类别"] = i.xpath(".//h3/a/text()").extract_first()

            #少儿图书的网页不一样，在这里要分开做(算了，不做了)
            if item["大类别"] == "少儿":
                continue
                #sm_url = i.xpath(".//h3/a/@href").extract_first()
                #yield scrapy.Request(url=sm_url, callback=self.c_page, meta={"item": deepcopy(item)})

            #提取小类别的url
            sm_url = i.xpath(".//h3/a/@href").extract_first()
            yield scrapy.Request(url=sm_url, callback=self.bg_url_details_page, meta={"item": deepcopy(item)})

    def bg_url_details_page(self, response):
        """全部小类"""
        item = response.meta["item"]
        #小类别分组
        a_list = response.xpath('//div[@id="search-path"]/dl//a')
        for i in a_list:
            item["小类别"] = i.xpath("./@title").extract_first()

            #提取小类别下详情页url
            sm_details_url = "https:" + i.xpath("./@href").extract_first()
            yield scrapy.Request(url=sm_details_url, callback=self.sm_details_page, meta={"item": deepcopy(item)})

    def sm_details_page(self, response):
        """详细小类"""
        item = response.meta["item"]
        li_list = response.xpath('//ul[@class="clearfix"]/li')

        #构造书的详情页url地址
        for a in li_list:
            details_url = "https:" + a.xpath('.//div[@class="img-block"]/a/@href').extract_first()
            yield scrapy.Request(url=details_url, callback=self.details_page, meta={"item": deepcopy(item)})

        #构造每个小类别的下一页地址
        for i in range(100):
            next_url = "https://list.suning.com/1-502325-{}-0-0-0-0-0-0-4.html".format(i)
            yield scrapy.Request(url=next_url, callback=self.parse, meta={"item": deepcopy(item)})



    def details_page(self, response):
        """图书详情页提取数据"""
        item = response.meta["item"]
        item["标题"] = response.xpath('//div[@class="proinfo-title"]/h1/text()').extract()
        item["标题"] = [re.sub(r"\s", "", i) for i in item["标题"]]  #多余字符去掉
        item["标题"] = [i for i in item["标题"] if len(i) > 0]  #去掉空字符

        item["作者"] = response.xpath('//div[@class="proinfo-main"]/ul/li[1]/text()').extract()
        item["作者"] = [re.sub(r"\s", "", i) for i in item["作者"]]  # 多余字符去掉
        item["作者"] = [i for i in item["作者"] if len(i) > 0]  # 去掉空字符

        item["出版社"] = response.xpath('//div[@class="proinfo-main"]/ul/li[2]/text()').extract()
        item["出版社"] = [re.sub(r"\s", "", i) for i in item["出版社"]]  # 多余字符去掉
        item["出版社"] = [i for i in item["出版社"] if len(i) > 0]  # 去掉空字符

        item["大图"] = "https:" + response.xpath('//div[@class="imgzoom-main"]/a/img/@src').extract_first()

        item["服务"] = response.xpath('//dd[@id="proinfo-id"]/span[position()>2]/a//text()').extract()
        item["服务"] = [re.sub(r"\s", "", i) for i in item["服务"]]  # 多余字符去掉
        item["服务"] = [i for i in item["服务"] if len(i) > 0]  # 去掉空字符

        #print(item)
        yield item


    def c_page(self, response):
        """处理少儿类别的图书"""
        pass
        #item = response.meta["item"]
        #div_list = response.xpath('//div[@class="banner-nav"]/div[position()<4]')
        #for i in div_list:
            #item["小类别"] = i.xpath('./div/h4/a/text()').extract()
            #print(item)

