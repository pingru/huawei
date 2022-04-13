# encoding=utf8
"""
editor:lenovo
date:2022year04month13day
"""
'''
描述
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

输入描述：
输入一行，为一个只包含小写字母的字符串。

输出描述：
输出该字符串反转后的字符串。

示例1
输入：
abcd

输出：
dcba
'''


# print(input()[::-1])
def reverse_str(string):
    if string.islower() and string.encode('utf-8').isalpha and len(string) <= 1000:  # 判断是否都是小写,判断是否都是字母,判断长度小于1000否
        return string[::-1]
    else:
        return '重新输入'


print(reverse_str(input()))
