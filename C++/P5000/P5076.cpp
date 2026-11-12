//题目描述
//您需要写一种数据结构，来维护一些数（都是绝对值 109  以内的数）的集合，最开始时集合是空的。其中需要提供以下操作，操作次数 q 不超过 104 ：
//定义数 x 的排名为集合中小于 x 的数的个数 +1。查询数 x 的排名。注意 x 不一定在集合里。
//查询排名为 x(x≥1) 的数。保证集合里至少有 x 个数。
//求 x 的前驱（前驱定义为小于 x，且最大的数）。若不存在则输出 −2147483647。
//求 x 的后继（后继定义为大于 x，且最小的数）。若不存在则输出 2147483647。
//插入一个数 x，本题的数据保证插入前 x 不在集合中。
//保证执行 1,3,4 操作时，集合中有至少一个元素。
//输入格式
//第一行是一个整数 q，表示操作次数。
//接下来 q 行，每行两个整数 op,x，分别表示操作序号以及操作的参数 x。
//输出格式
//输出有若干行。对于操作 1,2,3,4，输出一个整数，表示该操作的结果。
//输入输出样例
//输入 #1复制
//7
//5 1
//5 3
//5 5
//1 3
//2 2
//3 3
//4 3
//输出 #1复制
//2
//3
//1
//5


#include <bits/extc++.h>
using namespace __gnu_pbds;

typedef tree<
    long long,
    null_type,
    std::less<long long>,
    rb_tree_tag,
    tree_order_statistics_node_update
> ordered_set;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    ordered_set sl;

    for (int i = 0; i < n; ++i) {
        int op;
        long long x;
        std::cin >> op >> x;

        if (op == 1) {
            // 查询 x 的排名（第几小）= 严格小于 x 的个数 + 1
            long long p = sl.order_of_key(x);
            std::cout << p + 1 << '\n';
        } else if (op == 2) {
            // 查询第 x 小（x 从 1 开始）
            auto it = sl.find_by_order(x - 1);
            std::cout << *it << '\n';
        } else if (op == 3) {
            // 前驱：严格小于 x 的最大值
            long long p = sl.order_of_key(x);
            if (p == 0) {
                std::cout << -2147483647LL << '\n';
            } else {
                auto it = sl.find_by_order(p - 1);
                std::cout << *it << '\n';
            }
        } else if (op == 4) {
            // 后继：严格大于 x 的最小值
            long long p = sl.order_of_key(x + 1);
            if (p == (long long)sl.size()) {
                std::cout << 2147483647LL << '\n';
            } else {
                auto it = sl.find_by_order(p);
                std::cout << *it << '\n';
            }
        } else {
            // op == 5：插入 x
            sl.insert(x);
        }
    }
    return 0;
}






