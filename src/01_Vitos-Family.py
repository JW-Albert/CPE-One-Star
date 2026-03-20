# https://onlinejudge.org/external/100/10041.pdf

'''本題的目標是輸出從 Vito Deadstone 的新家 到所有親戚家的最小距離和為多少。
輸入測資的第一列有一個整數，代表接下來有幾組測資。
每組測資的第一個整數r代表親戚的數目。 (0 < r < 500)
接下來的r個整數 (s1,s2,…,sr) 代表各個親戚的門牌號碼。(0 < s < 30000)。
注意，親戚的門牌號碼可能會相同。'''

import sys

line1 = int(sys.stdin.readline())

if line1:
    for _ in range(line1):
        data = list(map(int ,sys.stdin.readline().split()))
        
        n = data[0]
        streets = data[1:]
        streets.sort()

        mid = streets[n // 2]

        res = 0
        for i in streets:
            res += abs(i - mid)

        print(res)