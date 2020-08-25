# Enter your code here. Read input from STDIN. Print output to STDOUT

en = int(input())
es = list(map(int, input().split()))
fn = input()
fs = list(map(int, input().split()))
a = es + fs
a = set(a)
print(len(a))
