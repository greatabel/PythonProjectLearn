from scrapy.selector import Selector
from scrapy.http import HtmlResponse


body = '''
<html>
    <head>
    <base href="http://example.com" />
    <title>example website</title>
    </head>

    <body>
    <div id='image'>

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
sel = response.xpath('//a')[0]
print(sel)
print('''
# 假设我们想选中当前这个a 后代中的所有img，下面的做法是错误的，
# 会找到文档中所有的img
# 因为//img是绝对路径，会从文档的根开始搜索，而不是从当前的a 开始
      ''')
print(sel.xpath('//img') )

print('需要使用.//img 来描述当前节点后代中的所有img')
print(sel.xpath('.//img') )
