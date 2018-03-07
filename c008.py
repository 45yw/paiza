l = []
import re

l = input().split()
s = input()
print(l)
match = re.search(r'<b>(.+)</b>', s)
if match:
    print(match.group(0))  # 検索パターン全体に一致する文字列
    print(match.group(1))  # 検索パターン中の括弧で囲まれた部分に一致する文字列
