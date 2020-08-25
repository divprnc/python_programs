if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if query_name == i:
            a = sum(student_marks[query_name])
            avg = a/3
    print("%.2f"% avg)
