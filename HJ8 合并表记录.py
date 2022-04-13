# encoding=utf8
"""
editor:lenovo
date:2022year04month13day
"""
'''
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

示例1
输入：
4
0 1
0 2
1 2
3 4

输出：
0 3
1 2
3 4
***************************
示例2
输入：
3
0 1
0 2
8 9

输出：
0 3
8 9
'''
n = input()  # 先输入的n代表,我要输入几行
dic = {}
for i in range(int(n)):
    line = input().split()
    # 输入格式本事就是空格来隔开,直接split()函数默认为空格的,函数返回列表line,且元素为子字符串
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key, 0) + value
    # 注意dic.get(key,0),如果字典中key对应有键值对,取对应的值value,如果没有这个键值对,那么函数get()返回值为0
    # 这一行的创建键值对,同时实现了,值的合并
for key in sorted(dic):  # sorted()函数直接传入字典,就是对字典的键进行排序,函数输出是键升序的一个列表list
    print(key, dic[key])
