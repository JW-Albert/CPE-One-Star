# https://onlinejudge.org/external/104/10420.pdf

'''核心任務
題目會給你一串名單，每一行包含一個國家名稱，後面跟著一個女性的名字。
你的任務是：統計每個國家分別出現了幾次（也就是唐璜在該國家征服了幾個人）。按照國家名稱的 字母順序（Alphabetical Order） 輸出國家與次數。
輸入與輸出規則
輸入：第一行是一個整數 n，代表總共有幾筆資料。接下來有 n 行，
每行第一個單字是國家，剩下的部分是名字（名字可能包含空格）。
輸出：每一行輸出「國家名稱」加上「出現次數」，中間用空格隔開。國家必須按 A 到 Z 的順序排列。'''

import sys

n = int(input())
country_diec = {}

for _ in range(n):
    line = sys.stdin.readline().split()
    if not line: continue

    country = line[0]

    country_diec[country] = country_diec.get(country ,0) + 1

for output in sorted(country_diec.keys()):
    print(f"{output} {country_diec[output]}")