import re

n = int(input())
for i in range(n):
    num = input()
    m = re.findall("(^[789]\d{8}).*", num)
    if m:
        print("YES")
    else:
        print("NO")
