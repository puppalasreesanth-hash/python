name = input("Enter student name: ")
marks = int(input("Enter aggregate marks: "))
subject = int(input("Enter subject marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))

if marks >= 75 and subject >= 60 and attendance >= 75 and income <= 200000:
    print("Scholarship Eligible")
else:
    print("Not Eligible")

