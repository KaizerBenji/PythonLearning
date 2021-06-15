#Exam 1 - Practical Exercise
#Created by: Benjamin Gray

while True:
    try:
        number = int(input("Input a number: "))
        break
    except ValueError:
        print("That is not a number. Try again.")