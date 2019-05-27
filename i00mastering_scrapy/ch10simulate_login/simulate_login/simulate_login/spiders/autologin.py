# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class AutologinSpider(scrapy.Spider):
    name = 'autologin'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile?_next=/places/default/index']

    def parse(self, response):
            # 解析登录后下载的页面，此例中为用户个人信息页面
            keys = response.css('table label::text').re('(.+):')
            values = response.css('table td.w2p_fw::text').extract()
            print('#'*20, keys, '@'*5, values)
            yield dict(zip(keys, values))
    # ----------------------------登录---------------------------------
    # 登录页面的url
    login_url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        # 登录页面的解析函数，构造FormRequest对象提交表单
        fd = {'email': 'greatabel1@126.com', 'password': 'LwV7kya3aKkyJ'}
        yield FormRequest.from_response(response, formdata=fd,
                                                 callback=self.parse_login)
    def parse_login(self, response):
        print('-'*10, 'parse_login')
        # 登录成功后，继续爬取start_urls 中的页面
        if 'Welcome great' in response.text:
            print('^-^ '*10)
            yield from super().start_requests() # Python 3语法

