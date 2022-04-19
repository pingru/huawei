# encoding=utf8
"""
editor:lenovo
date:2022year04month14day
"""
'''
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足 1≤n≤10000  ，坐标保证满足 -2^{31} <= x,y <= 2^{31}-1，且数字部分仅含正数
输入描述：
一行字符串

输出描述：
最终坐标，以逗号分隔

示例1
输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;

输出：
10,-10

示例2
输入：
ABC;AKL;DA1;

输出：
0,0
'''
#方法1:
input_list = input().split(';')
initial = [0,0]

for item in input_list:
    if not 2 <= len(item) <= 3:
        continue

    try:
        direction = item[0]
        step = int(item[1:])
        if direction in ['A', 'D', 'W', 'S']:
            if 0 <= step <= 99:
                if direction == 'A':
                    initial[0] -= step
                elif direction == 'D':
                    initial[0] += step
                elif direction == 'S':
                    initial[1] -= step
                elif direction == 'W':
                    initial[1] += step
    except:
        continue

print(str(initial[0]) + ',' + str(initial[1]))

#方法2:
while True:
    try:
        position_list = input().split(';')
        direction = {'A': 1, 'D': 2, 'W': 3, 'S': 4}  # 方向规则
        x, y = 0, 0  # 起点位置
        for i in range(len(position_list)):
            tmp = position_list[i]  # 第i个指令
            if not tmp:
                continue  # 题目中的+一个空 不影响那段,如果指令是空,将继续下一个循环
            judge = direction.get(tmp[0])
            # tmp[0]合法指令的第一位,那个字母,如果direction规则中存在这个指令字母,取其指令值,
            # 如果不存在,函数get()的返回值是None
            if judge and len(tmp) <= 3:  # 指令合法
                number = -1
                try:
                    number = int(tmp[1:])  # 取指令后面两位数字
                except:
                    pass
                if number >= 0:  # 指令中的数值都是正值
                    if judge == 1:
                        x -= number  # 坐标左移
                    elif judge == 2:
                        x += number  # 坐标右移
                    elif judge == 3:
                        y += number  # 坐标上移
                    else:
                        y -= number  # 坐标下移
        print(x, end=',')
        print(y)
    except:
        break

