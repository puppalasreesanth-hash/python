teams = ["Team A", "Team B", "Team C"]
points = [6, 9, 6]
scores = [10, 15, 12]

for i in range(3):
    print(teams[i], "Points:", points[i],
          "Score:", scores[i])

for i in range(3):
    for j in range(i + 1, 3):
        if points[j] > points[i] or (points[j] == points[i] and scores[j] > scores[i]):
            points[i], points[j] = points[j], points[i]
            scores[i], scores[j] = scores[j], scores[i]
            teams[i], teams[j] = teams[j], teams[i]

print("\nFinal Rankings")

for i in range(3):
    print(i + 1, teams[i], points[i], "Points")
