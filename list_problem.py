
size = int(input())
lst1 = []

for i in range(size):
    lst1.append(int(input()))

lst1.sort()
print(lst1)
lst = []
a = len(lst1)
b = lst1[0]
c = lst1[a-1]
while b<=c:

    lst.append(b)
    b = b + 1

print(lst)


