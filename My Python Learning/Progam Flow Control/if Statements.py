name = input("Please enter your name: ") #user inputs name
age = int(input("How old are you, {0}? ".format(name))) #user inputs age. Must be an integer or it will break
print(age)

if age >= 18: #starting a block of code
    print("You are old enough to vote!")
    print("Please put an X in the box next to your choice!")
else:
    print("Please come back in {0} years.".format(18 - age))

if age < 18:
    print("Please come back in {0} years.".format(18 - age))
else:
    print("You are old enough to vote!")
    print("Please put an X in the box next to your choice!")