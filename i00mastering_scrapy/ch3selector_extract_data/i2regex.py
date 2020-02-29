from scrapy.selector import Selector
from scrapy.http import HtmlResponse


body = '''
<html>
    <body>
    <h1>Hello world 0</h1>
    <h1>Hello world 1</h1>
    <b>Hello world 2</b>

    <ul>
    <li>Python <b> 价格：99.0 元</b></li>
    <li>R <b> 价格：199.0 元</b></li>
    <li>Swift <b> 价格：299 元</b></li>
    <li>Swift <b> 价格：399 元</b></li>
    </ul>
    </body>
</html>

'''

response = HtmlResponse(url='htttp://www.example.com',
            body=body, encoding='utf-8')
selector = Selector(response=response)

li_selctors = selector.xpath('.//li/b/text()')
print(li_selctors)

# 只提取价格的float 数字部分
prices = selector.xpath('.//li/b/text()').re('\d+\.\d+')
print(prices)
# 提取出float和int
prices = selector.xpath('.//li/b/text()').re('\d*\.?\d+')
print(prices)

first = selector.xpath('.//li/b/text()').re_first('\d+\.\d+')
print('first=', first)

