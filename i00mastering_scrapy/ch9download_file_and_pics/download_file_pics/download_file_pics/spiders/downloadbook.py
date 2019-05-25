# -*- coding: utf-8 -*-
import scrapy


class DownloadbookSpider(scrapy.Spider):
    name = 'downloadbook'
    allowed_domains = ['www.juzimi.com']
    start_urls = ['https://www.juzimi.com/meitumeiju']

    def parse(self, response):
        item = {}
        # 下载列表
        item['file_urls'] = []
        for url in response.xpath('/html/body//img/@src').extract():
            download_url = response.urljoin(url)
            #将url填入下载列表
            print('#'*10, url[2:])
            item['file_urls'].append(download_url)
