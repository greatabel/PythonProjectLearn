import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib as mpl
import pprint
from i0positions import Positions
import i1netmode
from scipy.optimize import curve_fit
from math import sqrt

"""
主要工作：用于分析从无线传感器网络获得的 RSSI 数据。 
分析无线传感器网络的信号强度和可视化热图中的数据以识别强信号强度和弱信号强度的区域非常有用
具体来说，我们拆分成4个story：

1.导入必要的库并从 CSV 文件中读取数据集
2.定义用于查找网络中每个点的平均 RSSI 值以及为每个网络节点的 RSSI 数据拟合曲线的函数
3.定义一个函数，用于绘制每个网络节点的 RSSI 值的热图，使用颜色图来表示值
4.遍历数据集中的每个网络节点，找到网络中每个点的平均 RSSI 值，将曲线拟合到 RSSI 数据，并使用定义的函数绘制 RSSI 值的热图
5.为每个网络节点创建一个新的 CSV 文件，其中包含网络中每个点的平均 RSSI 值


拟合图部分：
当我们在测量无线信号时，我们经常需要将接收到的信号强度（RSSI）转换成距离或者其他指标。
这通常涉及到建立一个数学模型，该模型可以将接收到的RSSI值与距离之间的关系联系起来。

我们使用了一种叫做“曲线拟合”的技术，该技术可以将一组数据拟合成一个函数。
在这里，我们将RSSI值作为y轴坐标，将距离值作为x轴坐标，并使用matplot绘制了一个曲线拟合图。

通过这个曲线拟合图，我们可以看到RSSI与距离之间的关系，从而可以使用这个关系来计算距离或者其他指标。
例如，当我们接收到一个未知距离的信号时，我们可以使用这个关系来估计距离，并将估计的距离与实际测量值进行比较，
以确保我们的计算是准确的。
Curve fitting 图可以帮助我们更好地理解RSSI与距离之间的关系，并使用这个关系来计算距离或者其他指标

"""
Node_coords = {
    "ap": (-7.3, 15),
    "hub0": (-2.3, 16),
    "hub1": (2.3, 6),
    "hub2": (0.2, 10),
}

dataset = pd.read_csv("data/i1processed_localhall.csv", header=[0, 1, 2])


features = np.asarray(dataset.iloc[:, 3:])
labels = np.asarray(dataset["Relative Position"])
headers = list(dataset)

labels = labels.flatten()  # all labels in an array
points = list(set(labels))  # unique labels
x = [Positions[str(point)]["Position_X"] for point in points]
y = [Positions[str(point)]["Position_Y"] for point in points]


print(dataset.head())


print(dataset.describe())


def return_mean(network_rssi):
    sums = {}
    counts = {}
    i = 0
    for label in labels:
        if network_rssi[i] != 100:
            if label not in sums:
                sums[label] = network_rssi[i]
                counts[label] = 1
            else:
                sums[label] += network_rssi[i]
                counts[label] += 1
        i += 1

    means = []
    for point in points:
        if point in sums and str(point) in Positions:
            means.append(sums[point] / counts[point])
        else:
            means.append(-100)

    return means


ap_rssi = dataset["ap"].values
plt.hist(ap_rssi, bins=20)
plt.xlabel("RSSI")
plt.ylabel("Frequency")
plt.title("Histogram of RSSI Values for AP Network")
plt.show()

hub0_rssi = return_mean(dataset["hub0"].values)
plt.scatter(x, y, c=hub0_rssi)
plt.colorbar()
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Scatterplot of RSSI Values for Hub0 Network")
plt.show()


def return_mean(network_rssi):
    sums = {}
    counts = {}
    i = 0
    for label in labels:
        if network_rssi[i] != 100:
            if label not in sums:
                sums[label] = network_rssi[i]
                counts[label] = 1
            else:
                sums[label] += network_rssi[i]
                counts[label] += 1
        i += 1

    for label in counts:
        sums[label] /= counts[label]

    for point in points:
        if point not in sums:
            sums[point] = -100

    return [sums[point] for point in points]


def func(d, n, C):

    return -10 * n * np.log10(d) + C


def find_optimal_curve_and_plot(network, network_mean_rssi):

    x1 = Node_coords[network][0]
    y1 = Node_coords[network][1]
    distances = [sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) for (x2, y2) in zip(x, y)]

    popt, pcov = curve_fit(func, distances, network_mean_rssi)

    print(popt)
    plt.plot(distances, network_mean_rssi, "bo-", label="data")
    plt.plot(
        distances,
        func(distances, *popt),
        "r-",
        label="fit: n=%5.3f, C=%5.3f" % tuple(popt),
    )
    plt.title("Curve fitting for {}".format(network))
    plt.xlabel("distance")
    plt.ylabel("rssi")
    plt.legend()
    # plt.show()
    # plt.draw()
    # plt.waitforbuttonpress(0)  # this will wait for indefinite time
    # plt.close()
    plt.show()


def plot_heatmap(network, network_mean_rssi):

    fig, ax = plt.subplots()  # note we must use plt.subplots, not plt.subplot
    i1netmode.plot_atmosphere(ax)

    cm = plt.cm.get_cmap("hot")
    my_cmap = cm(np.linspace(0, 1, len(network_mean_rssi)))
    rects = []
    simple_plot = True
    if simple_plot:
        sc = plt.scatter(x, y, c=network_mean_rssi, s=250, marker="s", cmap=cm)
        plt.colorbar(sc)

    else:  # better plot but freaking messy
        for i in range(len(x)):
            if i <= 13:
                rect = Rectangle((x[i] - 0.5, y[i] - 1), 1, 2.5, color=my_cmap[i])
            else:
                rect = Rectangle((x[i] - 0.5, y[i] - 0.5), 1, 1, color=my_cmap[i])
            rects.append(rect)
            ax.add_patch(rect)
        minx = min(network_mean_rssi)
        maxx = max(network_mean_rssi)
        N = len(network_mean_rssi)
        norm = mpl.colors.Normalize(vmin=minx, vmax=maxx)
        sm = plt.cm.ScalarMappable(cmap=cm, norm=norm)
        sm.set_array([])
        plt.colorbar(sm)

    plt.title("RSSI Map of {}".format(network))
    # plt.show()
    # plt.draw()
    # plt.waitforbuttonpress(0)  # this will wait for indefinite time
    # plt.close(fig)
    plt.show()



plot = True
if plot:
    networks = [network for network in Node_coords]
    # network = networks[1] #'ca-access-point'
    for network in networks:
        # network rssi values
        network_rssi = np.asarray(dataset[network]).flatten()
        # network rssi mean value by point in order of points
        network_rssi_mean = return_mean(network_rssi)

        find_optimal_curve_and_plot(network, network_rssi_mean)
        plot_heatmap(network, network_rssi_mean)

create_mean_csv = True
if create_mean_csv:
    mean_csv = {}

    first = [i for i in headers if "Relative Position" in i][0]  # relative header
    second = [i for i in headers if "Position X" in i][0]  # relative header
    third = [i for i in headers if "Position Y" in i][0]  # relative header
    mean_csv[first] = points
    mean_csv[second] = x
    mean_csv[third] = y

    for network in Node_coords:
        head = [i for i in headers if network in i][0]  # relative header
        # network rssi values
        network_rssi = np.asarray(dataset[network]).flatten()
        # network rssi mean value by point in order of points
        network_rssi_mean = return_mean(network_rssi)
        mean_csv[head] = network_rssi_mean

    df = pd.DataFrame(mean_csv)
    df.to_csv("data/i2processed_average_positions.csv", na_rep="100", index=False)

"""
[  1.11697398 -37.72039195]
[  0.66802839 -35.55425655]
[  2.35996152 -37.62381845]
[  3.20808451 -29.93974698]

"""
