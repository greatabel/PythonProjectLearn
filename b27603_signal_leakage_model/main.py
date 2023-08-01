import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

# 定义频率范围
freq = rf.Frequency(start=700, stop=700, npoints=1, unit='mhz')

# 定义电缆的特性
cable = rf.media.DefinedGammaZ0(freq, z0=[50], gamma=[0.02])

# 定义一个由四个点组成的路径
path = np.array([[0, 0], [50, 50], [100, 50], [150, 100]])

# 计算每一段的长度
lengths = np.sqrt(np.sum(np.diff(path, axis=0)**2, axis=1))

# 计算总长度
total_length = np.sum(lengths)

# 定义路径损耗和噪声模型
def path_loss(distance, path_loss_exponent):
    return (distance)**path_loss_exponent

# 定义噪声模型
def noise_model(distance, noise_factor):
    return np.random.normal(scale=noise_factor, size=distance)

# 对每一段进行信号损耗模拟，并考虑增加发射功率的策略
powers = [1, 2, 5, 10]  # 发射功率，单位W
for power in powers:
    losses = []
    gains = []
    for length in lengths:
        ntwk = cable.line(length, 'm', loss=True)
        loss = ntwk.s21
        loss_db = 20*np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10*np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        gain = 10*np.log10(power) - total_loss_db
        gains.append(gain)
    for gain in gains:
        plt.plot(np.arange(len(gain)), gain, label=f'Power={power}W')
plt.xlabel('Segments')
plt.ylabel('Loss (dB)')
plt.title('Signal Loss and Gain in a Bending Path')
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
        ntwk = cable.line(length, 'm', loss=True)
        loss = ntwk.s21
        loss_db = 20*np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10*np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        gain = 10*np.log10(power) - total_loss_db
        gains.append(gain)
    for gain in gains:
        plt.plot(np.arange(len(gain)), gain, label=f'Power={power}W')
plt.show()

# 对整个路径进行信号损耗模拟，并考虑改变电缆的物理参数的策略
gammas = [0.02, 0.01, 0.005, 0.002]  # 电缆的传播常数

loss_matrix = np.zeros((len(gammas), len(lengths)))  # 用于存储不同gamma和路径长度下的损失

for i, gamma in enumerate(gammas):
    cable = rf.media.DefinedGammaZ0(freq, z0=[50], gamma=[gamma])
    losses = []
    for j, length in enumerate(lengths):
        ntwk = cable.line(length, 'm', loss=True)
        loss = ntwk.s21
        loss_db = 20*np.log10(np.abs(np.squeeze(loss.s)))
        path_loss_db = 10*np.log10(path_loss(length, path_loss_exponent=2))
        noise_db = noise_model(int(length), noise_factor=2)
        total_loss_db = loss_db + path_loss_db + noise_db
        losses.append(total_loss_db)
        loss_matrix[i, j] = total_loss_db

# 生成热图
plt.figure(figsize=(10, 7))
plt.imshow(loss_matrix, cmap='hot', interpolation='nearest')
plt.colorbar(label='Loss (dB)')
plt.xlabel('Path Lengths')
plt.ylabel('Gamma')
plt.title('Heatmap of Signal Loss')
plt.xticks(np.arange(len(lengths)), np.round(lengths, 2))
plt.yticks(np.arange(len(gammas)), gammas)
plt.show()


