# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem
import re

class LagouZhaopinSpider(scrapy.Spider):
    name = 'lagou_zhaopin'
    allowed_domains = ['lagou.com']
    start_urls = ["https://www.lagou.com/zhaopin/1/"]

    def parse(self, response):
        li_list = response.xpath("//li[@class='con_list_item default_list']")
        for i in li_list:
            data_dict = LagouItem()
            data_dict["title"] = i.xpath(".//h3/text()").extract()
            data_dict["addr"] = i.xpath(".//span[@class='add']/em/text()").extract()

            #提取详情页数据
            detail_url = i.xpath('.//a[@class="position_link"]/@href').extract_first()
            yield scrapy.Request(
                                detail_url,
                                callback=self.parse_detail,
                                meta={"data_dict": data_dict}
                                )

        # 请求下一页
        #extract_first()得到的是str类型
        next_page_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        print(next_page_url)
        if next_page_url != "javascript:;":
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):  #详情页数据提取
        data_dict = response.meta["data_dict"]

        #去掉多余字符（空表，换行等）
        content_list = response.xpath('//*[@id="job_detail"]/dd[2]/div//text()').extract()
        content_list = [re.sub(r"\s", "", i) for i in content_list]  #将多余字符替换成空字符
        data_dict["detail"] = [i for i in content_list if len(i) > 0]  #去掉空字符
        yield data_dict
