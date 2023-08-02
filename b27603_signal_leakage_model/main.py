import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from i1best_strategy import *

from i2common import *

# 对每一段进行信号损耗模拟，并考虑增加发射功率的策略
powers = [1, 2, 5, 10]  # 发射功率，单位W
for power in powers:
    losses = []
    gains = []
    for length in lengths:
        ntwk = cable.line(length, "m", loss=True)
        loss = ntwk.s21
        loss_db = 20 * np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10 * np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        gain = 10 * np.log10(power) - total_loss_db
        gains.append(gain)
    for gain in gains:
        plt.plot(np.arange(len(gain)), gain, label=f"Power={power}W")
plt.xlabel("Segments")
plt.ylabel("Loss (dB)")
plt.title("Signal Loss and Gain in a Bending Path")
plt.grid(True)
plt.legend()
plt.show()


# 对整个路径进行信号损耗模拟，并考虑改变电缆的物理参数的策略
# 对每一段进行信号损耗模拟，并考虑增加发射功率的策略
powers = [1, 2, 5, 10]  # 发射功率，单位W
for power in powers:
    losses = []
    gains = []
    for length in lengths:
        ntwk = cable.line(length, "m", loss=True)
        loss = ntwk.s21
        loss_db = 20 * np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10 * np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        gain = 10 * np.log10(power) - total_loss_db
        gains.append(gain)
    for gain in gains:
        plt.plot(np.arange(len(gain)), gain, label=f"Power={power}W")
plt.show()

# 对整个路径进行信号损耗模拟，并考虑改变电缆的物理参数的策略
gammas = [0.02, 0.01, 0.005, 0.002]  # 电缆的传播常数

loss_matrix = np.zeros((len(gammas), len(lengths)))  # 用于存储不同gamma和路径长度下的损失

noise_scale = 0.1
for i, gamma in enumerate(gammas):
    cable = rf.media.DefinedGammaZ0(freq, z0=[50], gamma=[gamma])
    for j, length in enumerate(lengths):
        ntwk = cable.line(length, "m", loss=True)
        loss = ntwk.s21
        loss_db = 20 * np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10 * np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        total_loss_db = total_loss_db + np.random.normal(scale=noise_scale)

        random_walk = 0

        if isinstance(total_loss_db, np.ndarray):
            if total_loss_db.size == 0:
                random_walk += np.random.normal(scale=noise_scale)
                loss_matrix[i, j] = random_walk
            elif total_loss_db.size == 1:
                loss_matrix[i, j] = total_loss_db.item()
            else:
                random_walk += np.random.normal(scale=noise_scale)
                loss_matrix[i, j] = random_walk
            # print("total_loss_db is not a scalar.")


# 生成热图
plt.figure(figsize=(10, 7))
plt.imshow(loss_matrix, cmap="hot", interpolation="nearest")
plt.colorbar(label="Loss (dB)")
plt.xlabel("Path Lengths")
plt.ylabel("Gamma")
plt.title("Heatmap of Signal Loss")
plt.xticks(np.arange(len(lengths)), np.round(lengths, 2))
plt.yticks(np.arange(len(gammas)), gammas)
plt.show()


# 信号损耗中加入一个随机的噪声项。使用numpy库中的随机数生成函数来实现这个功能


def white_noise(signal, noise_level):
    noise = np.random.normal(scale=noise_level, size=signal.shape)
    return signal + noise


noise_level = 0.1
for power in powers:
    losses = []
    gains = []
    for length in lengths:
        ntwk = cable.line(length, "m", loss=True)
        loss = ntwk.s21
        loss_db = 20 * np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10 * np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        # 添加white noise
        total_loss_db = white_noise(total_loss_db, noise_level)
        gain = 10 * np.log10(power) - total_loss_db
        gains.append(gain)
    for gain in gains:
        plt.plot(np.arange(len(gain)), gain, label=f"Power={power}W")


plt.legend(loc="upper right")
plt.show()


print("------最优的信号传输策略-----")

# 设置初始功率，学习率和迭代次数
initial_power = 1.0
learning_rate = 0.01
num_iterations = 1000

# 计算初始功率下的平均损失
initial_loss = loss_function(initial_power, lengths)
print(f"The average loss with initial power is {initial_loss}dB")

# 执行梯度下降优化
optimal_power = gradient_descent(
    loss_function, initial_power, learning_rate, num_iterations, lengths
)

# 计算优化后的平均损失
optimal_loss = loss_function(optimal_power, lengths)
print(f"The average loss with optimal power is {optimal_loss}dB")

# 输出最优功率
print(f"The optimal power is {optimal_power}W")


# 计算使用初始功率和最优功率时的平均损耗
average_loss_initial_power = initial_loss
average_loss_optimal_power = optimal_loss

# 使用初始功率和最优功率作为x轴的标签
labels = ["Initial Power", "Optimal Power"]

# 使用平均损耗作为y轴的值
values = [average_loss_initial_power, average_loss_optimal_power]

# 创建一个新的图形
plt.figure()

# 创建一个条形图
plt.bar(labels, values)

# 添加y轴标签
plt.ylabel("Average Loss (dB)")

# 添加图形标题
plt.title("Comparison of Average Loss for Initial and Optimal Power")

# 显示图形
plt.show()

"""
The average loss with initial power is -25.148274876489825dB
The average loss with optimal power is -44.80259987262122dB
The optimal power is 0.01W
损耗比例（也就是原始的功率和经过传输后的功率之比）是小于1的。这是可以理解的，因为在无线通信中，信号在传输过程中总是会有一定的损耗。

损耗常常用分贝（dB）来表示，而分贝值可以是正的也可以是负的。分贝是一种对数表示法，
它是10倍对数值的比例（即，dB = 10*log10（比例））。
如果比例大于1，那么对应的dB值就是正的；如果比例小于1，那么对应的dB值就是负的

"""
