name = input("Please enter your name: ") #user inputs name
age = int(input("How old are you, {0}? ".format(name))) #user inputs age. Must be an integer or it will break
print(age)

if age < 18:
    print("Please come back in {0} years.".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in return to the Jedi :( ")
else:
    print("You are old enough to vote!")
    print("Please put an X in the box next to your choice!")