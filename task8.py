
name = input("Enter student name: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
lab = int(input("Enter lab marks: "))

risk = 0

if marks < 40:
    print("Low Marks Risk")
    risk += 1

if attendance < 75:
    print("Low Attendance Risk")
    risk += 1

if lab < 40:
    print("Low Lab Marks Risk")
    risk += 1

if risk == 0:
    print("Category: No Risk")
elif risk == 1:
    print("Category: Medium Risk")
else:
    print("Category: High Risk")

print("Total Risk Factors:", risk)
