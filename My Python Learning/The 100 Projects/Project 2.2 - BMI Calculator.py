# BMI Calculator
height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
bmi = float(weight * 703) / float(height ** 2)
bmi_as_int = (round(bmi, 2))
print(bmi_as_int)
