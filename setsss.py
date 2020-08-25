a = int(input())
sa = set(map(int, input().split()))
fn = int(input())
for i in range(fn):
    a, *b = input().split()
    if a == "intersection_update":
        c = set(map(int, input().split()))
        sa &= c
    elif a == "update":
        d = set(map(int, input().split()))
        sa.update(d)
    elif a == "symmetric_difference_update":
        e = set(map(int, input().split()))
        sa.symmetric_difference_update(e)
    elif a == "difference_update":
        f = set(map(int, input().split()))
        sa.difference_update(f)

print(sum(sa))



s