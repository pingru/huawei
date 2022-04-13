# encoding=utf8
"""
editor:lenovo
date:2022year04month12day
"""
'''
描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。

示例1
输入：
hello nowcoder

输出：
8

说明：
最后一个单词为nowcoder，长度为8   
'''


def get_len():
    str_in = input()
    lis = str_in.split()  # split()函数默认是按照空格进行划分
    if len(lis) == 0 or len(lis) > 5000:
        return '请重新输入'
    else:
        return len(lis[-1])  # 取最后一个单词的长度


print(get_len())
