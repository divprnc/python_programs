if __name__ == '__main__':
    lst = []
    for i in range(int(input())):
        lst.append([])
        name = input()
        score = float(input())
        lst[i].append(name)
        lst[i].append(score)

    a = []
    b = len(lst)
    for i in range(b):
        a.append(lst[i][1])

    s = sorted(set(a))[1]

    for n,m in sorted(lst):
        if m == s:
            print(n)

