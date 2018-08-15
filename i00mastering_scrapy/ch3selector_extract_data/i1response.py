from scrapy.selector import Selector
from scrapy.http import HtmlResponse


body = '''
<html>
    <body>
    <h1>Hello world 0</h1>
    <h1>Hello world 1</h1>
    <b>Hello world 2</b>

    <ul>
    <li>Python</li>
    <li>R</li>
    <li>Swift</li>
    </ul>
    </body>
</html>

'''

response = HtmlResponse(url='htttp://www.example.com',
            body=body, encoding='utf-8')
selector = Selector(response=response)

selector_list = selector.xpath('//h1')
print(selector_list)