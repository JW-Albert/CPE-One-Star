# https://onlinejudge.org/external/109/10929.pdf

'''Step 1. 題目概要
核心任務題目會給你一個非常大的正整數（最多可達 1000 位數），請你判斷這個數字是否為 11 的倍數。
輸入與輸出規則輸入：每行一個正整數 $N$。
當輸入為 0 時，代表程式結束。
輸出：如果是 11 的倍數，輸出：N is a multiple of 11.如果不是，輸出：N is not a multiple of 11.
注意：輸出格式必須包含原始的數字 $N$。
Step 2. 解題思路雖然 Python 可以直接處理超大整數（直接用 % 11 == 0 判斷），但在演算法競賽中，通常希望你使用倍數判別法，這樣即使在不支援大數運算的語言（如 C++）中也能輕鬆解題。11 的倍數判別法：奇偶位數差一個數字是否能被 11 整除，取決於：(奇數位數之和) 與 (偶數位數之和) 的差，是否為 11 的倍數（包含 0）。'''

x = int(input())
while x != 0:

    if x % 11 == 0:
        print(x ,"is a multiple of 11.")
    else:
        print(x ,"is not a multiple of 11.")

    x = int(input())