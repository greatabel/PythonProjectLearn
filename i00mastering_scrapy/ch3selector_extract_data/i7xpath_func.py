from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import mycolor


text_content = '<a href="#">click here to go to the \
        <strong>Next Page</strong></a>'
sel = Selector(text=text_content)
print(sel)
print(sel.xpath('/html/body/a/strong/text()'))
print(mycolor.show('same as 使用string函数:'), 
    sel.xpath('string(/html/body/a/strong)').extract())