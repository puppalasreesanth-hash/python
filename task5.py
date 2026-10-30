t1 = ("Monday", "9:00", "10:00", "Room A")
t2 = ("Monday", "9:30", "10:30", "Room B")

print("Timetable 1:", t1)
print("Timetable 2:", t2)

if t1[0] == t2[0] and t1[2] > t2[1] and t1[1] < t2[2]:
    print("Time Conflict Detected!")
else:
    print("No Time Conflict")

if t1[3] == t2[3]:
    print("Room Conflict Detected!")
else:
    print("Rooms are Available")

