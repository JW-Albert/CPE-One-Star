# https://onlinejudge.org/external/100/10055.pdf
import sys

for line in sys.stdin:
    data = line.split()
    if not data:
        continue

    x ,y = map(int ,data)

    print(abs(x - y))