# -*- coding: utf-8 -*-
import scrapy


class AutologinSpider(scrapy.Spider):
    name = 'autologin'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        pass
