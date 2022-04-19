# encoding: utf-8
'''
输入字符串中出现次数最多的字母,及其出现次数
'''
# s = input()  # 输入字符串
# s = 'abaaa'
s = input()
dic = {}
for i in s:
    dic[i] = dic.get(i, 0) + 1
# print(dic)
key = sorted(dic)[0]
print(key)
print(dic.get(key))
