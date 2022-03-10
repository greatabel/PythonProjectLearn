from utils import COLOR, DIRECTION


class AnalysisData:
    """分析颜色以及方向信息，给下位机传字符通信

    Returns：
        a: 绿色，左转
        b: 绿色，右转
        c: 红色，左转
        d: 红色，右转
        e: 没有检测到箭头
    """

    def __init__(self, ret, color, dirt):
        self.ret = ret
        self.color = color
        self.dirt = dirt

    def analysisData(self):

        if not self.ret:
            return "e"

        if self.color == COLOR.GREEN:
            if self.dirt == DIRECTION.LEFT:
                return "a"
            else:
                return "b"
        else:
            if self.dirt == DIRECTION.LEFT:
                return "c"
            else:
                return "d"
