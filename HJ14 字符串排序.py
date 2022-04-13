# encoding=utf8
"""
editor:lenovo
date:2022year04month13day
"""
'''
描述
给定 n 个字符串，请对 n 个字符串按照字典序排列。

数据范围： 1≤n≤1000  ，字符串长度满足 1≤len≤100 
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入：
9
cap
to
cat
card
two
too
up
boat
boot

输出：
boat
boot
cap
card
cat
to
too
two
up
'''


def fun():
    n = int(input())  # 默认键盘输入为字符串
    l = []
    for i in range(n):  # range(n),只能传入数字
        x = input()
        l.append(x)
    for i in sorted(l):  # sorted()函数本身返回值就是一个按字典顺序排好的列表
        print(i)


fun()
