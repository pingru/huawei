# encoding=utf8
"""
editor:lenovo
date:2022year04month12day
"""
'''
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串

示例1
输入：
abc

输出：
abc00000
'''
string = input()


def str_split(string):
    res = []
    while len(string) > 8:  # 输入字符串长度大于8时
        res.append(string[:8])  # 直接将字符串前8位截断的子字符串(字符串切片)存入列表res,作为一个元素
        string = string[8:]  # 将列表替换为8位后面的全部字符的子字符串(字符串切片),再进行循环
    res.append('{:0<8}'.format(string))  # '{:0<8}'.format,是在字符串右侧补0,总宽度为8的意思
    return res


fin = str_split(string)  # 函数返回的结果res是一个列表,每个元素都是一个小字符串
for i in fin:
    print(i)  # 将列表的每个元素,按行输出
