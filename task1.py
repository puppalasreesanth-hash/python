units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 200 + (units - 100) * 3
else:
    bill = 500 + (units - 200) * 5

fixed = 50
total = bill + fixed

print("Electricity Bill:", total)
month1 = int(input("Enter previous month bill: "))
month2 = total

if month2 > month1 * 1.5:
    print("Unusual increase in bill!")
else:
    print("Normal bill")
