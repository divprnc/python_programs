class Rank:
    def __init__(self,semester,grade,credit):
        self.semester = semester
        self.grade = grade
        self.credit = credit
    def Sgpa(self):
        sgpa = sum(self.grade)/self.credit
        print("SGPA :",sgpa)


def calculate(grade):
    if grade == "S" or grade == "s":
        return 10
    elif grade == "A" or grade == "a":
        return 9
    elif grade == "B" or grade == "b":
        return 8
    elif grade == "C" or grade == "c":
        return 7
    elif grade == "D" or grade == "d":
        return 6
    elif grade == "E" or grade == "e":
        return 5
    elif grade == "F" or grade == "f":
        return 0
    else:
        print("Invalid Grade")


all_subjects = []
all_credit = 0
sem = int(input("Enter Your Semester: "))
sub = int(input("Enter Total Subjects: "))
for _ in range(sub):
    credit = float(input("Enter Credit: "))
    all_credit += credit
    grade = input("Enter Grade: ")
    cd = calculate(grade)
    all_subjects.append((credit*cd))

student = Rank(sem,all_subjects,all_credit)
student.Sgpa()

