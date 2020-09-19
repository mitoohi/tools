"""
定义了一些常用的数值计算函数方法
"""

import math

from number_calculate.prime import get_numbers


# 求信息熵
def calc_entropy():
    numbers = get_numbers()
    entropy = 0
    for item in numbers:
        entropy -= item[1] * math.log(item[1], 2)
    print('prob is :', [i[1] for i in numbers])
    print('entropy = ', entropy, 'bits')


if __name__ == '__main__':
    pass
