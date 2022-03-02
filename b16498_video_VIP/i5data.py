import json

class SourceDataDemo:

    def __init__(self):
        self.title = 'liziqi大数据可视化展板'
        self.counter = {'name': '粉丝讨论', 'value': 41000}
        self.counter2 = {'name': '日常更新', 'value': 5000}
        self.echart1_data = {
            'title': 'twitter情绪分布',
            'data': [
                {"name": "num_positive", "value": 120},
                {"name": "num_neural", "value": 30},
                {"name": "num_nagtive", "value": 100},

            ]
        }
        self.echart2_data = {
            'title': 'twitter中文圈关联词分布',
            'data': [
                {"name": "歌曲", "value": 10},
                {"name": "art", "value": 4},
                {"name": "中国", "value": 3},
                {"name": "生活", "value": 3},
                {"name": "娱乐", "value": 2},
       
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '网红视频分布',
            'data': [
                {"name": "娱乐", "value": 10},
                {"name": "旅游", "value": 20},
                {"name": "做饭", "value": 20},
                {"name": "经济", "value": 30},
                {"name": "生活", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "中国艺术", "value": 4},
                {"name": "中国文化", "value": 5},
                {"name": "中国经济", "value": 9},
                {"name": "中国军事", "value": 8},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "环球新闻数", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "本地天津新闻数", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '新闻地域分布',
            'data': [
                {"name": "天津", "value": 19},
                {"name": "美国", "value": 12},
                {"name": "欧洲", "value": 10},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart6_data = {
            'title': '新闻地域分布比例',
            'data': [
                {"name": "天津", "value": 64, "value2": 36, "color": "01", "radius": ['59%', '70%']},
                {"name": "美国", "value": 76, "value2": 24, "color": "02", "radius": ['49%', '60%']},
                {"name": "欧洲", "value": 80, "value2": 20, "color": "03", "radius": ['39%', '50%']},
                {"name": "其他", "value": 82, "value2": 18, "color": "04", "radius": ['29%', '40%']},
               
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '天津', 'value': 239},
                {'name': '北京', 'value': 121},
                {'name': '其他', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = 'liziqi大数据可视化展板'

