k = int(input())
n = list(map(int, input().split()))
d = {}
for i in n:
    d[i] = d.get(i,0) + 1

for k,v in d.items():
    if v == 1:
        print(k)
        quit()

