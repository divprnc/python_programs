
n,m=map(int,input().split())
l=input().split(' ')
A=set(input().split(' '))
B=set(input().split(' '))
ha=0

for i in l:
    if i in A:
        ha+=1
    if i in B:
        ha-=1
print(ha)



