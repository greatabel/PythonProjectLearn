import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

from i2common import *


def gradient_descent(
    loss_function, initial_power, learning_rate, num_iterations, lengths
):
    power = initial_power

    for i in range(num_iterations):
        # 计算梯度
        gradient = (
            loss_function(power + 0.01, lengths) - loss_function(power, lengths)
        ) / 0.01

        # 更新 power
        power = power - learning_rate * gradient

        # 确保 power 值大于 0
        if power <= 0:
            power = 0.01

    return power


# 损失函数
def loss_function(power, lengths):
    losses = []
    # 对于每个长度
    for length in lengths:
        ntwk = cable.line(length, "m", loss=True)
        # 计算损失
        loss = ntwk.s21
        loss_db = np.mean(20 * np.log10(np.abs(np.squeeze(loss.s))))
        path_loss_db = np.mean(10 * np.log10(path_loss(length, path_loss_exponent=2)))
        noise_db = np.mean(noise_model(int(length), noise_factor=2))
        total_loss_db = loss_db + path_loss_db + noise_db
        gain = 10 * np.log10(power) - total_loss_db
        losses.append(gain)

    return np.mean(losses)
