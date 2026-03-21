# https://onlinejudge.org/external/102/10222.pdf

import sys

keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

text = sys.stdin.read()
text = list(text.lower())

result = []

for i in text:
    if i == ' ' or i == '\n':
        result.append(i)
    else:
        idx = keyboard.find(i)
        if idx != -1:
            result.append(keyboard[idx - 2])
        else:
            result.append(i)

print("".join(result) ,end="")