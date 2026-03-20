# https://onlinejudge.org/external/100/10035.pdf

'''Step 1. 題目概要
每列會給兩個數字，數字的長度不會超過10位數。且兩個數字的長度不一定會一樣。
輸入 0 0 時，表示結束。
當 進位總數量(count)等於0，輸出No carry operation.。
當 進位總數量(count)等於1，輸出1 carry operation.。
當 進位總數量(count)等於n (n>1)，輸出n carry operations.。
Step 2. 解題思路
專注於 當前進位(carry) 與 進位總數量(count) 的計算上。
當前進位(carry) 使用判斷式 a%10 + b%10 + carry >= 10 來進行判斷，a%10、b%10 表示分別取 a 與 b 的尾數，+ carry 表示 加 上一位的 進位(carry，carry 只會是 0 or 1)。
若判斷式為 true 則 carry=1 且 count++，若 false 則 carry=0。
最後判斷完成後使用 a/=10、b/=10 拋棄 a 與 b 的尾數。'''

import sys

for line in sys.stdin:
    x ,y = map(int ,line.split())

    if (x == 0 and y == 0):
        break

    carry_counter = 0
    carry_tmp = 0

    while (x > 0 and y > 0):
        a = x % 10
        b = y % 10

        if (a + b >= 10):
            carry_tmp = (a + b) // 10
            carry_counter += 1

        x = x // 10
        y = y // 10

        x += carry_tmp

    if carry_counter == 0:
        print("No carry operation.")
    elif carry_counter == 1:
        print("1 carry operation.")
    else:
        print(carry_counter ,"carry operations.")