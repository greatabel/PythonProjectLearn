from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import mycolor


text_content = '<div>\
                <p class="small info">hello world</p>\
                <p class="normal info">hello scrapy</p>\
                </div>'
sel = Selector(text=text_content)

contain_p = sel.xpath('//p[contains(@class, "small")]')
contain_info = sel.xpath('//p[contains(@class,"info")]')


print(contain_p)
print(contain_info)