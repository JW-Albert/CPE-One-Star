# https://onlinejudge.org/external/100/10008.pdf

'''規則細節：
不分大小寫：'a' 和 'A' 都算作同一個字母。
只統計字母：所有的標點符號（如 .、,、!）和數字都要忽略，不列入統計。
排序要求（這是本題最重要的地方）：
    優先按次數排序：出現次數越多的字母排在越前面。
    次數相同時：按字母的 ASCII 順序（也就是 A 到 Z 的順序）排列。
輸入與輸出範例：
輸入：第一行告知有幾行文字，接著是文字內容。
輸出：字母 次數（中間一個空格），例如 E 5、A 2。'''

import sys

n = int( sys.stdin.readline().strip() )

line = sys.stdin.read().splitlines()
text = "".join( line ).upper()


counts = {}

for i in text:
    if 'A' <= i <= 'Z':
        counts[i] = counts.get(i ,0) + 1

sotred_count = sorted( counts.items() ,key = lambda x: (-x[1] ,x[0]) )

for char ,count in sotred_count:
    print(f"{char} {count}")