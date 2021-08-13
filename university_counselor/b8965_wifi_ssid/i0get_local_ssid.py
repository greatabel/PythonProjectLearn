import subprocess
import re

# ABCMeta是Python的特殊的元类，用来生成抽象类
from abc import ABCMeta, abstractmethod
from termcolor import colored, cprint


# os类，定义say方法，但不实现
class OS(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


class Windows(OS):
    def say(self):
        print("i am windows")
        return windows_ssid()


class Mac(OS):
    def say(self):
        print("i am mac osx")
        return osx_ssid()


# 工厂类,简单工厂模式
# https://blog.csdn.net/likunkun__/article/details/93884508
class OperationSystemFactory(object):
    # say方法的统一接口，传入子类对象，调用他们的say方法
    def get_ssid(self, object_type):
        return eval(object_type)().say()


"""
在windows系统上，打开cmd命令窗口，执行命令
netsh wlan show network
这个命令就可以查看计算机可以连接的wifi网络

有了查看wifi的命令，就可以使用python的subprocess模块来执行这个命令


"""


def windows_ssid():
    # https://zhuanlan.zhihu.com/p/93835847
    result = subprocess.check_output(["netsh", "wlan", "show", "network"])
    result = result.decode("gbk")
    lst = result.split("\r\n")
    lst = lst[4:]
    results = []
    for index in range(len(lst)):
        if index % 5 == 0:
            results.append(lst[index])
            print(lst[index])
    # 只需要返回一个本机连接的ssid
    return resultss[0]
    """
    example results:

    SSID 1 : song189
    SSID 2 : CMCC-iGKK
    SSID 3 : CMCC-Mshj
    SSID 4 : 
    SSID 5 : Gtspc2018
    SSID 6 : CU_S36b
    SSID 7 : bear&fish
    SSID 8 : ziroom1102
    SSID 9 : Xiaomi_238A
    SSID 10 : xiangyu2102
    """


def osx_ssid():
    process = subprocess.Popen(
        [
            "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
            "-I",
        ],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    s = "".join(map(chr, out))
    print(s)
    pattern_s = " SSID:"
    pattern_e = " MCS:"

    start = re.search(pattern_s, s).span()[0]
    end = re.search(pattern_e, s).span()[0]
    ssid = s[start + 7 : end - 1].strip()
    text = colored(ssid, "red", attrs=["reverse", "blink"])
    print(text)
    return ssid


if __name__ == "__main__":

    ff = OperationSystemFactory()
    os = "Mac"
    ssid = ff.get_ssid(os)
    print("ssid=", ssid)
