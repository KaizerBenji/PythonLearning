# Program make a simple calculator

# This function finds the sum of two numbers.
def addition(a, b):
    total = a + b
    return round(total, 4)


# This function finds the difference of two numbers.
def subtraction(a, b):
    total = a - b
    return round(total, 4)


# This function find product of two numbers.
def multiplication(a, b):
    total = a * b
    return round(total, 4)


# This function finds the quotient of two numbers.
def division(a, b):
    total = a / b
    return round(total, 4)


print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    # User inputs the choice they would like to make.
    choice = input("Enter choice( 1 | 2 | 3 | 4 | 5 ): ")

    # Checks the user's input to see if it is valid.
    if choice in ("1", "2", "3", "4", "5"):
        if choice == "5":
            print("\n***Exiting Calculator***")
            exit()
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input and please start over!")
                break

            if choice == "1":
                print("The sum of {0} and {1}".format(num1, num2), "is", addition(num1, num2))

            elif choice == "2":
                print("The difference of {0} and {1}".format(num1, num2), "is", subtraction(num1, num2))

            elif choice == "3":
                print("The product of {0} and {1}".format(num1, num2), "is", multiplication(num1, num2))

            elif choice == "4":
                print("The quotient of {0} and {1}".format(num1, num2), "is", division(num1, num2))

            break
    else:
        print("Invalid Input, please try again!")
