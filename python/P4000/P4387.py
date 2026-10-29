# 题目描述
# 给出两个序列 pushed 和 poped 两个序列，其取值从 1 到 n(n≤100000)。已知入栈序列是 pushed，如果出栈序列有可能是 poped，则输出 Yes，否则输出 No。请注意，给定的序列一定是一个排列（即没有重复数字）。
#
# 为了防止骗分，每个测试点有多组数据，不超过 5 组。
#
# 输入格式
# 第一行一个整数 q，询问次数。
#
# 接下来 q 个询问，对于每个询问：
#
# 第一行一个整数 n 表示序列长度；
#
# 第二行 n 个整数表示入栈序列；
#
# 第三行 n 个整数表示出栈序列；
#
# 输出格式
# 对于每个询问输出答案。
#
# 输入输出样例
# 输入 #1复制
#
# 2
# 5
# 1 2 3 4 5
# 5 4 3 2 1
# 4
# 1 2 3 4
# 2 4 1 3
# 输出 #1复制
#
# Yes
# No
from collections import deque

m = int(input())

for _ in range(m):
    n = int(input())
    orig = list(map(int, input().split()))
    # print(orig)
    seq = {x: i for i, x in enumerate(orig)}  # 一个数在原数组中的位置
    stack = []
    i = 0
    now = list(map(int, input().split()))
    # print(now)
    flg = True
    for x in now:
        # print(x)
        while seq[x] >= i:
            stack.append(orig[i])
            i += 1
        if stack and stack[-1] == x:
            stack.pop()
            continue
        if seq[x] < i:
            flg = False
            break

    if flg:
        print('Yes')
    else:
        print('No')






