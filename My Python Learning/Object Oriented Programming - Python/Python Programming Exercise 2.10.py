print("Enter employee information to find weekly pay:")
wage = float(input("Enter the employees hourly wage: $"))
hours = int(input("Enter the employees hours for the week: "))
overTime = int(input("Enter the employees overtime hour: "))
pay = wage * hours
totalPay = pay + (wage * overTime * 1.5)
print("The employees total pay for the week is: $", (round(totalPay,2)))