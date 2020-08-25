# if __name__ == '__main__':
s = input()
# The any() method returns True if any element of an iterable is True. If
#  not, any() returns False.
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))
#
#  any() function take string one by one and validate any one of them are following
#  specialisations or not
n=7
m =21
p = '.|.'
l = n//2
# z = (2*i+1)
for i in range(n//2):
    print((p*(2*i+1)).center(m,'-'))
print(('WELCOME').center(m,'-'))
lst = []
for i in range(n//2):
    lst.append(str((p*(2*i+1)).center(m,'-')))
print(lst)
lst.reverse()
for i in range(len(lst)):
    print(lst[i])
# i = n//2
# pt = [(p*(2*i+1)).center(m,'-') for i in range(n//2)]
# print('\n' +str(pt[::-1]))
for z in range(0):
    print(z)