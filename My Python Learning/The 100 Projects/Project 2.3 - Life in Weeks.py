# Project 2.3 Life in Weeks
age = input("What is your current age: ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

life_remaining = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"

print(life_remaining)
