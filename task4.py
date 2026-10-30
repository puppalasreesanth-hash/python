
name = input("Enter student name: ")

m1 = int(input("Enter first exam marks: "))
m2 = int(input("Enter second exam marks: "))
m3 = int(input("Enter third exam marks: "))

average = (m1 + m2 + m3) / 3

print("Average Marks:", average)

if m3 > m1:
    print("Performance Improved")
elif m3 < m1:
    print("Performance Declined")
else:
    print("Performance Stable")

if average >= 75:
    print("Grade: Excellent")
elif average >= 50:
    print("Grade: Average")
else:
    print("Grade: Poor")

if m1 < 35 and m2 < 35 and m3 < 35:
    print("Consistently Weak Performance")
