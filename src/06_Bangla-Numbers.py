# https://onlinejudge.org/external/101/10101.pdf

'''Step 1. 題目概要
這題要求你把一個數字轉換成孟加拉語（Bangla）的計數單位。這跟我們中文的「個、十、百、千、萬、億」邏輯很像，只是單位名稱和進位方式不同。
孟加拉計數單位：
kuti = 10,000,000 (千萬，即 $10^7)
lakh = 100,000 (十萬，即 $10^5)
hajar = 1,000 (千，即 $10^3)
shata = 100 (百，即 $10^2)
輸入與輸出規則：
輸入：每行一個數字（最大可達 15 位數，這超過了 32-bit 整數的範圍，但在 Python 中沒問題）。
輸出：按照格式輸出 Case 序號. 轉換後的字串。序號要靠右對齊（寬度為 4）。如果數字是 0，也要輸出 0。'''

import sys

def convert(n):
    result = []

    if (n >= 10000000):
        result.extend( convert(n // 10000000) )
        result.append( "kuti" )
        n %= 10000000

    if (n >= 100000):
        result.append( str(n // 100000) )
        result.append( "lakh" )
        n %= 100000

    if (n >= 1000):
        result.append( str(n // 1000) )
        result.append( "hajar" )
        n %= 1000

    if (n >= 100):
        result.append( str(n // 100) )
        result.append( "shata" )
        n %= 100

    if (n > 0):
        result.append( str(n) )

    return result

case_num = 1
output = []

for line in sys.stdin:
    x = line.strip()

    if not x:
        continue

    x = int(line)

    if x != 0:
        output = convert(x)
    else:
        output = ["0"]

    print(f"{case_num:4}. {' '.join(output)}")

    case_num += 1