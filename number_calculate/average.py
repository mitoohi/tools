"""
计算平均数
"""
from number_calculate.prime import get_numbers


# 求和，求加权平均数
def weighted_average():
    numbers = get_numbers()
    wa, weight, s = 0, 0, 0
    for i in numbers:
        weight += i[1]
        wa += i[0] * i[1]
        s += i[0]
    print('your inputs is:')
    print('\tnumber\tweight')
    for i in numbers:
        print('\t', i[0], '\t', i[1])
    print('sum = ', s)
    print('weight_sum = ', wa)
    print('weighted_average = ', wa / weight)


if __name__ == '__main__':
    weighted_average()
