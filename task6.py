marks = [
    [80, 70, 90],
    [60, 50, 65],
    [90, 85, 95]
]

for i in range(3):
    print("Student", i+1, "Total:", sum(marks[i]))

for j in range(3):
    avg = (marks[0][j] + marks[1][j] + marks[2][j]) / 3
    print("Subject", j+1, "Average:", avg)

    if avg < 60:
        print("Low Average")

print("Top Student:", marks.index(max(marks)) + 1)
