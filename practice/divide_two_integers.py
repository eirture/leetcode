#!/usr/bin/env python
# coding=utf-8

"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def divide(dividend, divisor):
    is_negative = (dividend < 0) != (divisor < 0)
    if dividend < 0:
        dividend = -dividend
    if divisor < 0:
        divisor = -divisor

    i = 0
    step = divisor
    step_count = 1
    begin_reduce = False

    step_list = []
    index = 0
    while dividend >= divisor:

        # print(dividend, step)
        while dividend < step and index >= 0:
            step, step_count = step_list[index]
            index -= 1

        if index < 0 and dividend < step:
            break

        dividend -= step
        i += step_count

        if not begin_reduce:
            step_list.append((step, step_count))
            step += step
            step_count += step_count
            index = len(step_list) - 1

    if is_negative:
        return max(-i, -1 << 31)
    return min(i, (1 << 31) - 1)


def main():
    cases = [
        (10, 3, 3),
        (7, -3, -2),
        (4294967296, -1, -2147483648)
    ]

    for dd, dr, r in cases:
        result = divide(dd, dr)
        if result != r:
            print('{} / {} != {}, {}'.format(dd, dr, result, r))
            exit(-1)
    print('pass')


if __name__ == '__main__':
    main()
