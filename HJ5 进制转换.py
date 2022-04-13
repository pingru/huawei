# encoding=utf8
"""
editor:lenovo
date:2022year04month12day
"""
'''
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 1<=n<=2^32 - 1
输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。

示例1
输入：
0xAA

输出：
170
'''
while True:
    try:
        print(int(input(), 16))  # 16进制数,转换为10进制数,直接用int()函数转换就可以了 #int()函数默认转化为10进制数
    except:
        break
