# -*- coding: utf-8 -*-
import scrapy


class Demo1Spider(scrapy.Spider):
    name = "demo1"
    allowed_domains = ["python123.io"]
    start_urls = ['http://python123.io/']

    def parse(self, response):
        pass
