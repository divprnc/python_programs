def print_rangoli(n):
    # your code goes here
    a = 'abcdefghijklmnopqrstuvwxyz'
    lst = list()
    for i in range(n):
        s = "-".join(a[i:n])
        # print(s)
        lst.append(s[::-1] + s[1:])
        # print(lst)

    length = len(lst[0])
    lst.reverse()
    # print(length)
    for i in range(n - 1):
        print(lst[i].center(length, "-"))
    lst.reverse()
    for i in range(n):
        print(lst[i].center(length, "-"))
    # for i in range(n):
    #    print(lst[i])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)