"""
存放数值计算的一些通用方法
"""
import re

import numpy as np
from matplotlib import pyplot as plt


# 将输入字符串转换为数值对
def get_numbers():
    inputs = re.split(';', input("请输入数字（格式为：数值10,数值11;数值20,数值21;...）："))
    numbers = [(re.split(',', item)) for item in inputs]
    numbers = list(map(lambda x: (float(x[0]), float(x[1])), numbers))
    return numbers


# 输入多维数组，绘制曲线图，以第一维作为横坐标数值
def draw_line(numbers, method=0):
    if method == 0:
        dim = len(numbers[0])
        plot = [[]] * dim
        for item in numbers:
            for i in range(dim):
                plot[i].append(item[i])
        plt.plot(dim[0], dim[1])
        for i in range(2, dim):
            plt.plot(plot[i])
        plt.show()
    elif method == 1:
        for i in range(1, len(numbers)):
            plt.plot(numbers[0], numbers[i])
        plt.show()
    elif method == 2:
        x = np.linspace(numbers[0][0], numbers[0][1])
        Y = []
        for func in numbers[1]:
            Y.append([func(i) for i in x])
        temp = [x]
        temp.extend(Y)
        draw_line(temp, method=1)
    else:
        print('only support method : 0, 1, 2')
        raise KeyError


if __name__ == '__main__':
    a = np.linspace(-4, 4)
    b = np.sin(a)
    c = np.cos(a)
    draw_line((a, b, c), method=1)
