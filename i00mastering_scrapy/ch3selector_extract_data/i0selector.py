from scrapy.selector import Selector


text_content = '''
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

selector = Selector(text=text_content)
print(selector)