# Chapter 3: Projects
print("1.Is the triangle equilateral?")
# inputs
a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))
# checking the sides of the triangle
if (a == b) and (b == c):
    print("The triangle is equilateral.")
else:
    print("This triangle is not equilateral.")
print()

print("2.Is the triangle a right triangle?")
# inputs
a1 = int(input("Enter side A: "))
b1 = int(input("Enter side B: "))
c1 = int(input("Enter side C: "))

if (a1 * a1 + b1 * b1 == c1 * c1) or (b1 * b1 + c1 * c1 == a1 * a1) or (a1 * a1 + c1 * c1 == b1 * b1):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
print()

print("3. Guessing Game")
import math
import random

# inputs
small = int(input("Enter the small number: "))
large = int(input("Enter the large number: "))
count = int(math.ceil(math.log(large + 1)/math.log(2)))
i = 0
while i < count:
    myNumber = (small + large) // 2
    print("%d %d" % (small, large))
    print("Your number is %d: " % myNumber)
    choice = input("Enter =, <, or > : ")
    if choice == "=":
        print("Hooray, I got it in %d tries " % (i+1))
        break
    elif small == large:
        print("I am out of guesses, and you cheated!")
        break
    elif choice == "<":
        large = myNumber - 1
    elif choice == ">":
        small = myNumber + 1
        i = i + 1
        if i >= count:
            print("I am out of guesses, and you cheated")
print()

print("4. Bounciness Index")


def bounciness_index():
    height = float(input("How high was the ball dropped from: "))
    bounce_index = float(input("Enter the bounciness index: "))
    num_of_bounces = float(input("How many times did the ball bounce: "))

    distance = 0

    while num_of_bounces > 0:
        distance = (height + distance)
        height = (height + bounce_index)
        distance = (distance + height)
        num_of_bounces -= 1
        print("Total distance traveled was: ", distance)


bounciness_index()
print()
