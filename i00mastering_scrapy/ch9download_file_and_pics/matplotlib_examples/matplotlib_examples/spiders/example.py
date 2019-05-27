# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/']

    def parse(self, response):
        pass
