from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import mycolor

body = '''
        <html>
           <head>
                <base href='http://example.com/' />
                <title>Example website</title>
           </head>
           <body>
                <div id='images-1' style="width: 1230px;">
                    <a href='image1.html'>Name: Image 1 <br/><img src='image1.jpg' /></a>
                    <a href='image2.html'>Name: Image 2 <br/><img src='image2.jpg' /></a>
                    <a href='image3.html'>Name: Image 3 <br/><img src='image3.jpg' /></a>
                </div>
                <div id='images-2' class='small'>
                    <a href='image4.html'>Name: Image 4 <br/><img src='image4.jpg' /></a>
                    <a href='image5.html'>Name: Image 5 <br/><img src='image5.jpg' /></a>
                </div>
           </body>
        </html>
        '''

response = HtmlResponse(url='http://www.example.com', body=body, encoding='utf8')
print('“选中所有的img=>”', response.css('img'))
print('“选中所有base和title”', response.css('base, title'))
print('“E1 E2：选中E1后代元素中的E2元素”:', response.css('div img'))
print('“E1>E2：选中E1子元素中的E2元素”:', response.css('body>div'))
print('“[ATTR]：选中包含ATTR属性的元素”', response.css('[style]'))
print('“[ATTR=VALUE]：选中包含ATTR属性且值为VALUE的元素”', response.css('[id=images-1]'))

