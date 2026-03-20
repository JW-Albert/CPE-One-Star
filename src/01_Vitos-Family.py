# https://onlinejudge.org/external/100/10041.pdf
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