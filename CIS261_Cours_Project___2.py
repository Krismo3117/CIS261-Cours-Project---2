def input_date():
    from_date = input("Enter from date (mm/dd/yyyy): ")
    to_date = input("Enter to date (mm/dd/yyyy): ")
    return from_date, to_date

employee_data_list = []

while True:
    from_date, to_date = input_date()
    employee_name = input("Enter employee name: ")
    total_hours = float(input("Enter total hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    income_tax_rate = float(input("Enter income tax rate (as a decimal): "))

    employee_data = {
        "from_date": from_date,
        "to_date": to_date,
        "employee_name": employee_name,
        "total_hours": total_hours,
        "hourly_rate": hourly_rate,
        "income_tax_rate": income_tax_rate
    }
    employee_data_list.append(employee_data)

    another_employee = input("Do you want to enter another employee? (yes/no): ")
    if another_employee.lower() != "yes":
        break

def calculate_and_display(employee):
    from_date = employee["from_date"]
    to_date = employee["to_date"]
    employee_name = employee["employee_name"]
    total_hours = employee["total_hours"]
    hourly_rate = employee["hourly_rate"]
    income_tax_rate = employee["income_tax_rate"]

    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * income_tax_rate
    net_pay = gross_pay - income_tax

    print("From:", from_date)
    print("To:", to_date)
    print("Employee Name:", employee_name)
    print("Hours Worked:", total_hours)
    print("Hourly Rate:", hourly_rate)
    print("Gross Pay:", gross_pay)
    print("Income Tax Rate:", income_tax_rate)
    print("Income Tax:", income_tax)
    print("Net Pay:", net_pay)
    print("-" * 30)

    return gross_pay, income_tax, net_pay

totals = {
    "total_employees": 0,
    "total_hours": 0,
    "total_tax": 0,
    "total_net_pay": 0
}

for employee in employee_data_list:
    gross_pay, income_tax, net_pay = calculate_and_display(employee)
    totals["total_employees"] += 1
    totals["total_hours"] += employee["total_hours"]
    totals["total_tax"] += income_tax
    totals["total_net_pay"] += net_pay

print("Total Employees:", totals["total_employees"])
print("Total Hours Worked:", totals["total_hours"])
print("Total Income Tax:", totals["total_tax"])
print("Total Net Pay:", totals["total_net_pay"])

