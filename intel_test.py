# encoding=utf8
"""
editor:lenovo
date:2022year04month19day
"""
'''

'''
# lis = [9,8,7,6,5,0,1,2,4,3]
lis = [1, 3, 5, 6]


def check(lis, low, high):  # 获取最近的叶子节点
    i = low  # 初始化i为根节点位置
    j = 2 * i + 1  # j是i的左孩子
    while j <= high and j < ((high - 1) // 2):  # 判断左孩子节点是否越界
        if j + 1 <= high:  # 如果右孩子也没越界
            j = j + 1  # j指针换成右孩子
            i = j  # 向下看一层
            j = 2 * i + 1
        else:
            break
    print(j + 1)


check(lis, 0, len(lis))
