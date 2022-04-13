# encoding=utf8
"""
editor:lenovo
date:2022year04month12day
"""
'''
描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

数据范围：1≤n≤1000 
输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

示例1
输入：
ABCabc
A
输出：
2
'''


def get_num():
    str1 = input()
    str2 = input()
    num = 0
    if not (len(str2) == 1):  # 没有输入1个字符
        return '请重新输入'
    else:
        for i in str1.lower():
            if i == str2.lower():
                num += 1
    return num


print(get_num())
