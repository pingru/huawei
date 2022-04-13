# encoding=utf8
"""
editor:lenovo
date:2022year04month13day
"""
'''
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围： 1≤n≤10^8
  
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入：
9876673

输出：
37689
'''
def fun():
    a = input()
    res = '' #创建输出字符串的空字符串接收
    for i in range(len(a)):
        l = a[::-1] #字符串从右向左阅读,所以倒叙
        if l[i] not in res: #如果倒叙读到的字符,不在输出字符串res中,添加在输出字符串res的尾部
            res = res + l[i]
    return res

print(fun())