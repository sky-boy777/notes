# -*- coding: utf-8 -*-
from scrapy import signals
import random


class UserAgent:
    def process_request(self, request, spider):
       ua = random.choice(spider.settings.get("UA_LIST"))
       request.headers["User-Agent"] = ua

class aa:
    def process_response(self, request, response, spider):
        print(request.headers["User-Agent"])
        return response

