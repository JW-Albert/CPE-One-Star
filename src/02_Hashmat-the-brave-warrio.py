# https://onlinejudge.org/external/100/10055.pdf

'''Step 1. 題目概要
每行輸入包含兩個數字。這兩個數字分別表示Hashmat的軍隊或是對手的軍隊的士兵數量，兩者可能顛倒放置。
輸出兩方士兵數量的差距即可。
Step 2. 解題思路
把題目給的兩個數字相減再取絕對值即可。'''

import sys

for line in sys.stdin.readline():
    data = line.strip()
    if not data:
        continue

    data = line.split()

    x ,y = map(int ,data)

    print(abs(x - y))