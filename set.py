# Enter your code here. Read input from STDIN. Print output to STDOUT
s = []
for i in range(int(input())):
    c = input()
    if c not in s:
        s.append(c)
print(len(s))

