from scrapy.selector import Selector
from scrapy.http import HtmlResponse


body = '''
<html>
    <head>
    <base href="http://example.com" />
    <title>example website</title>
    </head>

    <body>
    <div id='images'>

    <a href='image00.html'>Name: Image 00 <br/><img src='image00.jpg' /></a>
    <a href='image01.html'>Name: Image 01 <br/><img src='image01.jpg' /></a>
    <a href='image02.html'>Name: Image 02 <br/><img src='image02.jpg' /></a>
    <a href='image03.html'>Name: Image 03 <br/><img src='image03.jpg' /></a>
    <a href='image04.html'>Name: Image 04 <br/><img src='image04.jpg' /></a>


    </div>

    </body>
</html>

'''

response = HtmlResponse(url='http://www.example.com',
                        body=body,
                        encoding='utf-8')
print('a的第3个：', response.xpath('//a')[2])
print('a的第3个：', response.xpath('//a[3]'))
print('a的最后1个：', response.xpath('//a[last()]'))
print('a的前3个:', response.xpath('//a[position()<=3]'))
print('包含id属性的div:', response.xpath('//div[@id]'))
print('包含id属性的div属性，并且值为images的div：', response.xpath('//div[@id="images"]'))