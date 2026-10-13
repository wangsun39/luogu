# 题目描述
# 呵呵，有一天我做了一个梦，梦见了一种很奇怪的电梯。大楼的每一层楼都可以停电梯，而且第 i 层楼（1≤i≤N）上有一个数字 K
# i （0≤K i ≤N）。电梯只有四个按钮：开，关，上，下。上下的层数等于当前楼层上的那个数字。当然，如果不能满足要求，相应的按钮就会失灵。例如：3,3,1,2,5 代表了 K
# i （K 1 =3，K 2 =3，……），从 1 楼开始。在 1 楼，按“上”可以到 4 楼，按“下”是不起作用的，因为没有 −2 楼。那么，从 A 楼到 B 楼至少要按几次按钮呢？
#
# 输入格式
# 共二行。
#
# 第一行为三个用空格隔开的正整数，表示 N,A,B（1≤N≤200，1≤A,B≤N）。
#
# 第二行为 N 个用空格隔开的非负整数，表示 K
# i 。
#
# 输出格式
# 一行，即最少按键次数，若无法到达，则输出 -1。
#
# 输入输出样例
# 输入 #1复制
#
# 5 1 5
# 3 3 1 2 5
# 输出 #1复制
#
# 3
# 说明/提示
# 对于 100% 的数据，1≤N≤200，1≤A,B≤N，0≤K
# i ≤N。
#
# 本题共 16 个测试点，前 15 个每个测试点 6 分，最后一个测试点 10 分。

from typing import List, Tuple
from heapq import *
from math import *
from collections import defaultdict

n, a, b = input().split()
n, a, b = int(n), int(a), int(b)
nums = input().split()
nums = [int(x) for x in nums]

# Dijkstra 算法模板
# g[x] = [y, w]
# 返回从 start 到每个点的最短路
def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[int]:
    # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
    dist = [inf] * n
    dist[start] = 0
    h = [(0, start)]
    while h:
        d, x = heappop(h)
        if d > dist[x]:
            continue
        for y, wt in g[x]:
            new_d = d + wt
            if new_d < dist[y]:
                dist[y] = new_d
                heappush(h, (new_d, y))
    return dist

g = defaultdict(list)

for i, x in enumerate(nums):
    if i + x < n:
        g[i].append([i + x, 1])
    if i - x >= 0:
        g[i].append([i - x, 1])

dist = dijkstra(g, a - 1, n)
if dist[b - 1] < inf:
    print(dist[b - 1])
else:
    print(-1)



