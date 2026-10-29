name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

gross_salary = basic + allowances + overtime + incentives

if gross_salary <= 20000:
    tax = gross_salary * 0.05
elif gross_salary <= 50000:
    tax = 1000 + (gross_salary - 20000) * 0.10
else:
    tax = 4000 + (gross_salary - 50000) * 0.15


pf = basic * 0.12
total_deductions = tax + pf

net_salary = gross_salary - total_deductions


print("\n========== SALARY STATEMENT ==========")
print(f"Employee Name     : {name}")
print(f"Employee ID       : {emp_id}")
print("--------------------------------------")
print(f"Basic Pay         : Rs. {basic:.2f}")
print(f"Allowances        : Rs. {allowances:.2f}")
print(f"Overtime          : Rs. {overtime:.2f}")
print(f"Incentives        : Rs. {incentives:.2f}")
print("--------------------------------------")
print(f"Gross Salary      : Rs. {gross_salary:.2f}")
print(f"Income Tax        : Rs. {tax:.2f}")
print(f"PF Deduction      : Rs. {pf:.2f}")
print(f"Total Deductions  : Rs. {total_deductions:.2f}")
print("--------------------------------------")
print(f"Net Salary        : Rs. {net_salary:.2f}")
print("======================================")

