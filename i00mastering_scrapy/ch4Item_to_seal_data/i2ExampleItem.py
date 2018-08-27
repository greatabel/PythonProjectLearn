from scrapy import Item, Field

class ExampleItem(Item):
    x = Field(a='hello', b=[1,2,3])
    y = Field(a=lambda x: x**2)

if __name__ == "__main__":
    print('“假设想传递额外信息给处理数据的某个组件”')
    e = ExampleItem(x=100, y=200)
    print(e, 'e.fields=', e.fields)

