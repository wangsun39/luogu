# 题目描述
# Caima 给你了所有 [a,b] 范围内的整数。一开始每个整数都属于各自的集合。每次你需要选择两个属于不同集合的整数，如果这两个整数拥有大于等于 p 的公共质因数，那么把它们所在的集合合并。
#
# 重复如上操作，直到没有可以合并的集合为止。
#
# 现在 Caima 想知道，最后有多少个集合。
#
# 输入格式
# 一行，共三个整数 a,b,p，用空格隔开。
#
# 输出格式
# 一个数，表示最终集合的个数。
#
# 输入输出样例
# 输入 #1复制
#
# 10 20 3
# 输出 #1复制
#
# 7
# 说明/提示
# 样例 1 解释
# 对于样例给定的数据，最后有 {10,20,12,15,18},{13},{14},{16},{17},{19},{11} 共 7 个集合，所以输出应该为 7。
#
# 数据规模与约定
# 对于 80% 的数据，1≤a≤b≤10
# 3
#  。
# 对于 100% 的数据，1≤a≤b≤10
# 5
#  ,2≤p≤b。

from typing import List, Tuple
from heapq import *
from math import *
from collections import defaultdict, deque
from bisect import *

def prime_factors(x, p):
    res = []
    i = 2
    while i * i <= x:
        if x % i != 0:
            i += 1
            continue
        if i >= p: res.append(i)
        while x % i == 0:
            x //= i
        i += 1
    if x >= p:
        res.append(x)
    return res

a, b, p = list(map(int, input().split()))


fa = {x: x for x in range(a, b + 1)}  # 另一种写法，x不连续
def find(x):
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]
def union(x, y):  # x 是代表元
    fa[find(y)] = find(x)


for x in range(a, b + 1):
    ps = prime_factors(x, p)
    for y in ps:
        z = x + y
        if z <= b:
            union(x, z)

for x in range(a, b + 1):
    find(x)

ans = len(set(fa.values()))


print(ans)







