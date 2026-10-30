students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    attendance = int(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    if marks >= 75 and attendance >= 75 and income <= 200000:
        students.append([name, marks])

students.sort(key=lambda x: x[1], reverse=True)

quota = 2

print("\nSelected Students:")

for i in range(min(quota, len(students))):
    print(students[i][0], students[i][1])

