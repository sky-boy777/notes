# -*- coding: utf-8 -*-
import scrapy
import json


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://list.suning.com/1-502325-0.html']

    def parse(self, response):
        """获取图书基本信息"""
        #分组
        li_list = response.xpath('//div[@id="filter-results"]/ul/li')
        for li in li_list:
            book_item = {}
            book_item["book_title"] = li.xpath('.//p[@class="sell-point"]/a/text()').extract_first()
            book_item["book_url"] = "https:" + li.xpath('.//p[@class="sell-point"]/a/@href').extract_first()

            #构造价格的url
            datasku = li.xpath('.//p[@class="prive-tag"]/em/@datasku').extract_first().split("|||||")
            book_item["book_price_url"] = "http://ds.suning.com/ds/generalForTile/{}_-781-2-{}-1--".format(datasku[0], datasku[1])
            yield scrapy.Request(
                book_item["book_price_url"],
                callback=self.book_price,
                meta={"book_item": book_item}
            )

        #构造下一页url
        page_num = response.xpath('//div[@id="bottom_pager"]/a[2]/text()').extract_first()
        next_url = "https://list.suning.com/1-502325-{}-0-0-0-0-14-0-4.html".format(page_num)
        #判断是否有下一页字样,
        text = response.xpath('//a[@id="nextPage"]/@title').extract_first()

        if text is not None:
            yield scrapy.Request(next_url, callback=self.parse)

    def book_price(self, response):
        """获取图书的价格"""
        book_item = response.meta["book_item"]
        rsp_dict = json.loads(response.body.decode())
        book_item["价格"] = rsp_dict["rs"][0]["price"]
        yield book_item

