# -*- coding: utf-8 -*-
import scrapy
import copy  # 每个方法间传递数据要用到深拷贝
import re
from scrapy_redis.spiders import RedisSpider   # 分布式爬虫继承的类

class FangSpider(RedisSpider):
    name = 'fang'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    # 将start_url插入redis,键为fang_url(lpush fang_url https://www.fang.com/SoufunFamily.htm)
    redis_key = "fang_url"

    def parse(self, response):
        # 只要我国的信息，最后一个是其它的，后面的页面不一样，所以之提取它之前的
        tr_list = response.xpath('//div[@class="outCont"]/table/tr[position()<last()]')
        sf = None  # 定义一个变量，用来存储“省份”
        for tr in tr_list:
            item = {}

            # 提取省份
            item["sf"] = tr.xpath('./td[@valign="top"]/strong/text()').extract_first()
            # 如果没有提取到省份，说明是前一个省份的，把之前定义好的变量sf给它
            if item["sf"] == "\xa0" or item["sf"] is None:
                item["sf"] = sf
            else:
                sf = item["sf"]

            # 提取城市
            a_list = tr.xpath('./td[last()]/a')
            for a in a_list:
                item["city"] = a.xpath('./text()').get()

                # 进入城市主页
                city_url = a.xpath('./@href').get()
                # 双重保险，保证运行不会出错
                city_url = response.urljoin(city_url)
                if city_url is not None:
                                                                                # 在这里要使用深拷贝，防止数据混乱
                    yield scrapy.Request(url=city_url, callback=self.city_page, meta={"item": copy.deepcopy(item)})


    def city_page(self, response):
        '''这里提取新房跟二手房的url链接然后请求'''
        item = response.meta["item"]

        # 进入买新房页面，注意：数据传递要用深拷贝
        new_house_url = response.xpath('//a[text()="买新房"]/@href').get()
        new_house_url = response.urljoin(new_house_url)
        if new_house_url is not None:
            yield scrapy.Request(url=new_house_url, callback=self.new_house, meta={"item": copy.deepcopy(item)})

        # 进入买二手房页面，数据传递同样要用深拷贝
        esf_url = response.xpath('//a[text()="买二手房"]/@href').get()
        esf_url = response.urljoin(esf_url)
        if esf_url is None:
            return
        yield scrapy.Request(url=esf_url, callback=self.esf, meta={"item": copy.deepcopy(item)})


    def new_house(self, response):
        '''新房页面信息提取'''
        pass
        item = response.meta["item"]
        item["类型"] = "新房"

        # 获取房子列表
        nhouse_list = response.xpath('//div[@class="nhouse_list"]/div/ul/li[contains(@id, "lp")]')
        for li in nhouse_list:
            # 小区标题
            item["title"] = li.xpath('.//div[@class="nlcd_name"]/a/text()').get().strip()

            # 居室跟平米
            jushi= li.xpath('.//div[contains(@class,"house_type")]//text()').getall()
            jushi = [re.sub(r'\s|/|－', '', i) for i in jushi]  # 将\n\t等字符替换为空字符
            item["type"] = [i for i in jushi if len(i) > 0]  # 去掉空字符

            # 地址
            item["addres"] = li.xpath('.//div[@class="address"]/a/@title').get()
            # 是否在售
            item["status"] = li.xpath('.//div[@class="fangyuan"]/span/text()').get()

            # 房子标题
            house_title = li.xpath('.//div[@class="fangyuan"]/a//text()').getall()
            house_title = [re.sub(r'\s|/|－', '', i) for i in jushi]  # 将\n\t等字符替换为空字符
            item["house_title"] = [i for i in jushi if len(i) > 0]  # 去掉空字符

            # 新房价格
            nhouse_price = li.xpath('.//div[@class="nhouse_price"]//text()').extract()  # 这里使用extract提取（不为别的，我喜欢）
            nhouse_price = "".join(nhouse_price)  # 把价格跟单位连成字符串
            item["price"] = nhouse_price.strip()  # 去掉两边空字符
            # 电话
            item["tel"] = "".join(li.xpath('.//div[@class="tel"]/p//text()').getall())
            # 房子详情url
            detail_url = li.xpath('.//div[@class="nlcd_name"]/a/@href').get()
            item["detail_url"] = response.urljoin(detail_url)

            yield item

        # 翻页
        next_page_url = response.xpath('//a[text()="下一页"]/@href').get()
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.new_house, meta={"item": copy.deepcopy(item)})
        else:
            # 这里因为有些页面没有下一页，所以只能获取全部的url，而且scrapy不会请求重复的url，这里不用担心
            all_url = list(set(response.xpath('//li[@class="fr"]/a/@href').getall()))
            for url in all_url:
                if url != "javascript:void(0)" or url is not None:
                    next_url = response.urljoin(url)
                    yield scrapy.Request(url=next_url, callback=self.new_house, meta={"item": copy.deepcopy(item)})


    def esf(self, response):
        '''二手房页面信息提取'''
        item = response.meta["item"]
        item["类型"] = "二手房"

        # 得到二手房列表，每一个dl一间房子
        dl_list = response.xpath('//div[@class="shop_list shop_list_4"]/dl')
        for dl in dl_list:
            # 小区标题
            item["title"] = dl.xpath('.//h4/a/@title').get()

            # 居室跟平米
            jushi = dl.xpath('.//p[@class="tel_shop"]//text()').getall()
            jushi = [re.sub(r'\s|/|－|\|', '', i) for i in jushi]  # 将\n\t等字符替换为空字符
            item["type"] = [i for i in jushi if len(i) > 0]  # 去掉空字符

            # 地址
            add_shop = dl.xpath('.//p[@class="add_shop"]//text()').getall()
            add_shop = [re.sub(r'\s|/|－|\|', '', i) for i in jushi]  # 将\n\t等字符替换为空字符
            item["address"] = [i for i in jushi if len(i) > 0]  # 去掉空字符

            # 总价格
            total_price = "".join(dl.xpath('.//dd[@class="price_right"]/span[@class="red"]//text()').getall())
            item["total_price"] = total_price.strip()
            # 每平米价格
            item["price"] = dl.xpath('.//dd[@class="price_right"]/span[last()]/text()').get()

            # 房子详情url
            detail_url = dl.xpath('.//h4/a/@href').get()
            item["detail_url"] = response.urljoin(detail_url)

            yield item

        # 翻页
        next_url = response.xpath('//a[text()="下一页"]/@href').get()
        if next_url is not None and next_url != "javascript:void(0)":
            # 在这里组合成完整链接，因为这里是已经过滤的了，能节省时间
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url, callback=self.esf, meta={"item": copy.deepcopy(item)})
        else:
            # 这里因为有些页面没有下一页，所以只能获取全部的url，而且scrapy不会请求重复的url，这里也不用担心
            all_url = list(set(response.xpath('//li[@class="fr"]/a/@href').getall()))  # 使用集合去下重保
            for url in all_url:
                if url != "javascript:void(0)" or url is not None:
                    next_url = response.urljoin(url)
                    yield scrapy.Request(url=next_url, callback=self.esf, meta={"item": copy.deepcopy(item)})




