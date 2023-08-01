import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from i1best_strategy import *

# 定义频率范围
freq = rf.Frequency(start=700, stop=700, npoints=1, unit="mhz")

# 定义电缆的特性
cable = rf.media.DefinedGammaZ0(freq, z0=[50], gamma=[0.02])

# 定义一个由四个点组成的路径
path = np.array([[0, 0], [50, 50], [100, 50], [150, 100]])

# 计算每一段的长度
lengths = np.sqrt(np.sum(np.diff(path, axis=0) ** 2, axis=1))

# 计算总长度
total_length = np.sum(lengths)

# 定义路径损耗和噪声模型
def path_loss(distance, path_loss_exponent):
    return (distance) ** path_loss_exponent


# 定义噪声模型
def noise_model(distance, noise_factor):
    return np.random.normal(scale=noise_factor, size=distance)
