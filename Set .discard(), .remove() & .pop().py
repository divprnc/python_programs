n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    a,*b = input().split()
    if a == 'pop':
        s.pop()
    elif a == 'remove':
        s.remove(int("".join(b)))
    elif a == 'discard':
        s.discard(int("".join(b)))

print(sum(s))


