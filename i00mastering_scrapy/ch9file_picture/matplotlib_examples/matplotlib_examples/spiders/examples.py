# -*- coding: utf-8 -*-
import scrapy


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplot.org']
    start_urls = ['http://matplot.org/']

    def parse(self, response):
        pass
