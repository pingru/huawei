# encoding=utf8
"""
editor:lenovo
date:2022year04month12day
"""
'''
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）


数据范围： 1<=n<=2*10^9+14
输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。

示例1
输入：
180

输出：
2 2 3 3 5
'''
# 方法2:
import math

n = int(input())
for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        print(i, end=' ')
        n = n / i  # 要整除赋值,不然会出现3613.0这种.0的数
if n > 2:
    print(n)  # 输入值是大质数的时候,它本身就是质因数,质因数不在其开方值math.sqrt(n)前面


# 思路清晰，对n做循环对2到(根号n)进行取余操作，如果余数为0就打印i，对n整除赋值。
# 循环走完，如果发现n还是大于2，则说明while循环一次都没跑，直接输出n为素数。


##########################################################################
# 方法1--->是不对的,不知道为什么:
def get_str(num):
    res = []  # 保存质因子的列表
    n = 2  # 从最小的质数开始尝试整除待除数num
    while num >= n:  # 当前待被处理的数,也可能就是质数,或者只要最后num被更新到是一个质数了,就截止了
        k = num % n
        if k == 0:
            res.append(str(n))  # 如果当前n可以将num进行整除,那么当前的n就是num的其中一个质因子,将此质因子保存到结果res列表中
            num = num / n  # 更新num值
        else:
            n = n + 1  # 如不能整除,将质数值进行增加,n=3之后,不用担心num还会被4整除,因为,如果它能被4整除,之前早就被2整除了,所以它不会再被4整除
    return ' '.join(res)  # 将已经被str()函数转换掉质因数n的数用空格连接


print(get_str(int(input())))  # 别忘了将输入字符用int()函数转成数字再进行处理
