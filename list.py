if __name__ == '__main__':
    lst = list()
    N = int(input())
    for i in range(N):
        a,*b = input().split()
        if a == "print":
            print(lst)
        elif a=="reverse":
            lst.reverse()
        elif a == "append":
            lst.append(int(b[0]))
        elif a =="sort":
            lst.sort()
        elif a == "remove":
            lst.remove(int(b[0]))
        elif a == "insert":
            i, e = int(b[0]), int(b[1])
            lst.insert(i, e)
        elif a== "pop":
            lst.pop()

