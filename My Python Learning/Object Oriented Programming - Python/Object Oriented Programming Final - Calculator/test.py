# Simple Calculator Program Created by Benjamin Gray

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


# This function is the Main Menu
def main_menu():
    print("\nWelcome to Benjamin Gray's Python Calculator,\nPlease Select an Operation from the Menu Below.\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")


while True:
    main_menu()  # Main Menu function is called.
    choice = input("Enter choice( 1 | 2 | 3 | 4 | 5 ): ")  # User inputs their choice
    # Checks the user's input to see if it is valid.
    if choice in ("1", "2", "3", "4", "5"):
        if choice == "5":  # User exits the calculator
            print("\n***Exiting Calculator***\n")
            input("**Press Enter to Exit**")
            exit()
        while True:
            try:
                num1 = float(input("\nEnter first number: "))  # User inputs first number
                num2 = float(input("\nEnter second number: "))  # User inputs second number
            except ValueError:
                print("\nInvalid input and please start over!")  # Error sends the User back to main menu
                break

            if choice == "1":  # Calls the addition func and uses the numbers the User input
                print("\nThe sum of {0} + {1}".format(num1, num2), "=", addition(num1, num2))
                input("\nPress Enter for Main Menu")

            elif choice == "2":  # Calls the subtraction func and uses the numbers the User input
                print("\nThe difference of {0} - {1}".format(num1, num2), "=", subtraction(num1, num2))
                input("\nPress Enter for Main Menu")

            elif choice == "3":    # Calls the multiplication func and uses the numbers the User input
                print("\nThe product of {0} * {1}".format(num1, num2), "=", multiplication(num1, num2))
                input("\nPress Enter for Main Menu")

            elif choice == "4":  # Calls the addition func and uses the numbers the User input
                print("\nThe quotient of {0} / {1}".format(num1, num2), "=", division(num1, num2))
                input("\nPress Enter for Main Menu")

            break  # Takes the User back to the Main Menu
    else:  # If input is not from "choice" then the user will receive this message and start over.
        print("Invalid Input, please try again!")


