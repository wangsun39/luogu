# 房间里放着 n 块奶酪。一只小老鼠要把它们都吃掉，问至少要跑多少距离？老鼠一开始在 (0,0) 点处。
# 输入格式
# 第一行有一个整数，表示奶酪的数量 n。
# 第 2 到第 (n+1) 行，每行两个实数，第 (i+1) 行的实数分别表示第 i 块奶酪的横纵坐标 xi,yi。
# 输出格式
# 输出一行一个实数，表示要跑的最少距离，保留 2 位小数。
# 输入输出样例
# 输入 #1复制
# 4 1 1 1 -1 -1 1 -1 -1
# 输出 #1复制
# 7.41
# 说明/提示
# 数据规模与约定
# 对于全部的测试点，保证 1≤n≤15，∣xi∣,∣yi∣≤200，小数点后最多有 3 位数字。
# 提示
# 对于两个点 (x1,y1)，(x2,y2)，两点之间的距离公式为 (x1−x2)2+(y1−y2)2。

from typing import List, Tuple
from heapq import *
from functools import lru_cache, cache
from math import *
from collections import defaultdict

MIN = lambda a, b: b if b < a else a

n = int(input())
nums = [[0] * 2 for _ in range(n)]
for i in range(n):
    x, y = input().split()
    nums[i][0], nums[i][1] = float(x), float(y)

nums.append([0, 0])

def dis(i, j):
    xi, yi = nums[i]
    xj, yj = nums[j]
    return ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5

# dp[i][mask]: 从 i 出发，走完 mask（mask 包含 i）中所有点，再回到原点 n 的最小距离
# 递推顺序：按 mask 中 1 的个数从小到大
dp = [[inf] * (1 << n) for _ in range(n)]

# 初始化：mask 只有一个点 i 时，从 i 直接回原点
for i in range(n):
    dp[i][1 << i] = dis(i, n)

# 按 mask 从小到大递推（mask 包含 i）
for mask in range(1, 1 << n):
    # 已经初始化过的单点情况跳过（其实也可以统一处理，但单点时下面循环不执行，保持 dis(i,n) 初值即可）
    if mask.bit_count() == 1:
        continue

    for i in range(n):
        if not (mask & (1 << i)):
            continue

        # 从 i 出发，下一步去 j（j 在 mask 中，且 j != i）
        res = inf
        rest = mask ^ (1 << i)
        for j in range(n):
            if rest & (1 << j):
                res = MIN(res, dis(i, j) + dp[j][rest])
        dp[i][mask] = res

ans = min(dp[i][(1 << n) - 1] for i in range(n))

print("%.2f" % ans)




