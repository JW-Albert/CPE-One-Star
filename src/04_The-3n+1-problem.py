# https://onlinejudge.org/external/1/100.pdf

'''Step 1. 題目概要
題目給定一個演算法，當 n 為 1 則結束，如果 n 是奇數則 n = 3*n+1，否則n = n/2。每一次遞迴都會打印一次 n。
給一個輸入 n ,透過以上的演算法我們可以得到一個數列（1作為結尾）。此數列的長度稱為 n 的 cycle-length。
例如輸入 n 為 22, 得到的數列： 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 ，則 22 的 cycle length 為 16。
輸入包含多列測資，每列有一對整數 i,j (0< i,j <1000000)。
Step 2. 解題思路
依照題目的說明製作遞迴式。'''

import sys

for line in sys.stdin:
    x ,y = map(int ,line.split())
    if x > y:
        x ,y = y ,x

    step = []

    for i in range(x ,y+1 ,1):
        num = i
        step_counter = 0

        while num != 1:
            step_counter += 1

            if num %2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
        
        step_counter += 1
        step.append(step_counter)

    print(x ,y ,max(step))