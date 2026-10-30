
readings = [
    [40, 50, 60],
    [70, 80, 90],
    [30, 40, 50]
]

total = 0
count = 0

for row in readings:
    for value in row:
        total += value
        count += 1

average = total / count

print("Average Reading:", average)
print("Highest Reading:", max(max(row) for row in readings))
print("Lowest Reading:", min(min(row) for row in readings))

if average <= 50:
    print("Environment: Good")
else:
    print("Environment: Poor")
