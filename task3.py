attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))

percentage = (attended / total) * 100

print("Current Attendance:", percentage, "%")

required = 75

if percentage >= required:
    print("You are eligible")
else:
    extra = 0
    while ((attended + extra) / (total + extra)) * 100 < required:
        extra += 1

    print("You need", extra, "more consecutive classes")
    print("Required attendance achieved!")
