D = {}

n = input("Enter Range:")
n = int(n)
for i in range(n):
    k = int(input("Enter USN:"))
    v = input("Enter name:")
    D[k] = v
print(list(sorted(D.items())))

print(list(reversed(sorted(D.items()))))