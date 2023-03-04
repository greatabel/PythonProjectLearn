import numpy as np
import matplotlib.pyplot as plt


def rmse(predictions, targets):
    predictions = np.array(predictions)
    targets = np.array(targets)
    return np.sqrt(((predictions - targets) ** 2).mean())


# 相对误差
def relative_func(predictions, targets):
    print("@" * 20, predictions, targets)
    predictions = np.array(predictions)
    targets = np.array(targets)
    return np.sqrt((predictions**2 + targets**2).mean())


# data/i3gps_error.csv 处理
# x为到房间大厅原点（正中间大门的距离）
x = [1, 2, 3, 4, 5, 6, 7, 8, 20, 30]
x = np.array(x)
print("x is :\n", x)
# gps误差测量的数据（米)

num = [89.4, 73.6, 50.5, 43.4, 44.9, 35.1, 24.2, 22.3, 15, 10]

y = np.array(num)
print("y is :\n", y)
# 用3次多项式拟合
f1 = np.polyfit(x, y, 3)
print("f1 is :\n", f1)

p1 = np.poly1d(f1)
print("p1 is :\n", p1)

# 也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  # 拟合y值
print("yvals is :\n", yvals)

accuracy_error = rmse(yvals, num)

relative = relative_func(yvals, num)
relative_error = accuracy_error / relative
print(
    "accuracy_error=",
    accuracy_error,
    "relative_error=",
    relative_error,
    "accuracy=",
    (1 - relative_error),
)

# 绘图
plot1 = plt.plot(x, y, "s", label="original values")
plot2 = plt.plot(x, yvals, "r", label="polyfit values")
plt.xlabel("distance-from-reference-point")
plt.ylabel("gps-distance-error")
plt.legend(loc=4)  # 指定legend的位置右下角
plt.title("polyfitting")
plt.show()

"""
          3         2
-0.3672 x + 4.882 x - 14.75 x + 31.55
yvals is :
 [21.31363636 18.63787879 21.31969697 27.15606061 33.94393939 39.48030303
 41.56212121 37.98636364]
@@@@@@@@@@@@@@@@@@@@ [21.31363636 18.63787879 21.31969697 27.15606061 33.94393939 39.48030303
 41.56212121 37.98636364] [17.4, 23.6, 30.5, 13.4, 34.9, 35.1, 54.2, 32.3]
accuracy_error= 8.10553963208328 relative_error= 0.17970559593956342 accuracy= 0.8202944040604365

"""
