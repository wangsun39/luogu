# 题目描述
# 贝茜听说一场特别的流星雨即将到来：这些流星会撞向地球，并摧毁它们所撞击的任何东西。她为自己的安全感到焦虑，发誓要找到一个安全的地方（一个永远不会被流星摧毁的地方）。
#
# 如果将牧场放入一个直角坐标系中，贝茜现在的位置是原点，并且，贝茜不能踏上一块被流星砸过的土地。
#
# 根据预报，一共有 M 颗流星 (1≤M≤50,000) 会坠落在农场上，其中第 i 颗流星会在时刻 T i （0≤Ti ≤1000）砸在坐标为 (Xi ,Yi )(0≤Xi ≤300，0≤Yi ≤300) 的格子里。流星的力量会将它所在的格子，以及周围 4 个相邻的格子都化为焦土，当然贝茜也无法再在这些格子上行走。
#
# 贝茜在时刻 0 开始行动，她只能在横纵坐标 X,Y≥0 的区域中，平行于坐标轴行动，每 1 个时刻中，她能移动到相邻的（一般是 4 个）格子中的任意一个，当然目标格子要没有被烧焦才行。如果一个格子在时刻 t 被流星撞击或烧焦，那么贝茜只能在 t 之前的时刻在这个格子里出现。 贝茜一开始在 (0,0)。
#
# 请你计算一下，贝茜最少需要多少时间才能到达一个安全的格子。如果不可能到达输出 −1。
#
# 输入格式
# 共 M+1 行，第 1 行输入一个整数 M，接下来的 M 行每行输入三个整数分别为 X i ,Yi ,Ti 。
#
# 输出格式
# 贝茜到达安全地点所需的最短时间，如果不可能，则为 −1。
#
# 输入输出样例
# 输入 #1复制运行
#
# 4
# 0 0 2
# 2 1 2
# 1 1 2
# 0 3 5
# 输出 #1复制运行
#
#

from typing import List, Tuple
from heapq import *
from math import *
from collections import defaultdict, deque

m = int(input())

r, c = 303, 303  # 隐藏陷阱： 超出边界的地方也是可以走的，而且都是安全的
pos = [[inf] * c for _ in range(c)]  # 标识位置是否是安全位置, inf 表示安全， 否则就是最早变成不安全的时间

arr = [[inf] * c for _ in range(c)]  # 标识到达位置的最早时间

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(m):
    x, y, t = input().split()
    t, x, y = int(t), int(x), int(y)
    pos[x][y] = min(pos[x][y], t)
    for dx, dy in dir:
        u, v = x + dx, y + dy
        if 0 <= u < r and 0 <= v < c:
            pos[u][v] = min(pos[u][v], t)

if pos[0][0] == inf:
    print(0)
    exit(0)
if pos[0][0] == 0:
    print(-1)
    exit(0)


arr[0][0] = 0

dq = deque([[0,0,0]])

while dq:
    x, y, t = dq.popleft()

    for dx, dy in dir:
        u, v = x + dx, y + dy
        if 0 <= u < r and 0 <= v < c and arr[u][v] > t + 1:
            if pos[u][v] == inf:
                print(t + 1)
                exit(0)
            if pos[u][v] > t + 1:
                arr[u][v] = t + 1
                dq.append([u, v, t + 1])


print(-1)



