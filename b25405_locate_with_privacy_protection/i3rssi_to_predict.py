import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pprint
from sklearn.neighbors import KNeighborsClassifier as kNN
from i0positions import Positions
import i1netmode

'''
读取i2visual_and_analysis.py生成的平均信号数据集，并将其转化为特征(features)和标签(labels)
使用 k-近邻分类器 (kNN) 建立模型 clf，并利用数据集对其进行训练
从网络中获取无线网络数据，并用已训练好的模型 clf 进行定位
计算定位误差，并用散点图在地图上表示出定位结果
提供了两个函数 rmse 和 relative_func 用于计算误差和相对误差
'''

def rmse(predictions, targets):
    predictions = np.array(predictions)
    targets = np.array(targets)
    return np.sqrt(((predictions - targets) ** 2).mean())


# 相对误差
def relative_func(predictions, targets):
    print("@" * 20, predictions, targets)
    predictions = np.array(predictions)
    targets = np.array(targets)
    return np.sqrt((predictions ** 2 + targets ** 2).mean())


plt.ion()
fig, ax = plt.subplots()  # note we must use plt.subplots, not plt.subplot
i1netmode.plot_atmosphere(ax)

dataset = pd.read_csv("data/i2processed_average_positions.csv", header=[0, 1, 2])
features = np.asarray(dataset.iloc[:, 3:])
labels = np.asarray(dataset["Relative Position"])

# MACs of networks in dataset
networks = [z for (_, _, z) in list(dataset)[3:]]

# If we want only selected wifis in dataset:
network_names = ["ap", "hub0", "hub1", "hub2"]
networks = [z for (x, _, z) in list(dataset)[3:] if x in network_names]
features = np.asarray(dataset[network_names])


found_networks = [0] * len(networks)

# a = dataset.hist()
# plt.plot(a)

clf = kNN(n_neighbors=2)
print("=====开始======")
print(clf)
clf.fit(features, labels)

# wifi_monitor = net.wifi_mon(interface = 'ap')
stop = False
while not stop:
    try:
        # cells = net.parse_scan(None, wifi_monitor)
        # print(cells)
        # unit test mock some test data
        cells = [
            {
                "bssid": "00:0b:6b:de:ea:36",
                "frequency": "2437",
                "signal level": "-37",
                "flags": "[WPA-PSK-TKIP][WPA2-PSK-TKIP][ESS]",
                "ssid": "hub0",
                "distance": "0.858",
            },
            {
                "bssid": "f4:ec:38:ed:14:25",
                "frequency": "2431",
                "signal level": "-47",
                "flags": "[WPA-PSK-TKIP][WPA2-PSK-TKIP][ESS]",
                "ssid": "hub1",
                "distance": "0.758",
            },
            {
                "bssid": "f4:ec:38:ed:10:fc",
                "frequency": "2432",
                "signal level": "-37",
                "flags": "[WPA-PSK-TKIP][WPA2-PSK-TKIP][ESS]",
                "ssid": "hub2",
                "distance": "0.658",
            },
        ]
        cell_realpositon = [-6, 15]
        # net.print_known_cells(cells)
        for i in range(len(found_networks)):
            found_networks[i] = 1
        for cell in cells:
            mac = cell["bssid"]
            if mac not in networks:
                continue
            rssi = cell["signal level"]
            found_networks[networks.index(mac)] = rssi
        print("-" * 20, found_networks, "-" * 20)
        position = clf.predict([found_networks])[0]

        pos = Positions[str(position)]
        pos_x = pos["Position_X"]
        pos_y = pos["Position_Y"]
        # plt.plot(pos_x, pos_y, marker='o', markersize=10, color="black")
        print("pos_x=", pos_x, "pos_y=", pos_y, "=>" * 20)
        accuracy_error = rmse([pos_x, pos_y], cell_realpositon)

        relative = relative_func([pos_x, pos_y], cell_realpositon)
        relative_error = accuracy_error / relative
        print(
            "accuracy_error=",
            accuracy_error,
            "relative_error=",
            relative_error,
            "accuracy=",
            (1 - relative_error),
        )

        marker = ax.scatter(pos_x, pos_y, marker="o", color="red")
        fig.canvas.draw()
        marker = ax.scatter(pos_x, pos_y, marker="o", color="black")
        # marker.remove()
        print("Position: {}".format(position))

    except KeyboardInterrupt:
        print("=====停止======")
        stop = True
        i1netmode.plot_atmosphere(ax)
        plt.ioff()
        plt.show()

# wifi_monitor.close()
"""
accuracy_error= 0.7071067811865476 relative_error= 0.0432337701167117 accuracy= 0.9567662298832883

"""
