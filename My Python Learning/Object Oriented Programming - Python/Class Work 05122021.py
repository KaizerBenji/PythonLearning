# Created by Benjamin Gray

x = "dog"
y = "cat"
xy = x + y
# Question 1
# x + y
# "The " + x " chases the " + y
# x * 4
print(xy)
print("The " + x +" chases the " + y)
print(x * 4)

# Question 2
# Write a string that contains your name and address on separate lines using embedded newline characters.
# Then write the same string literal without the newline characters.
firstString = "Benjamin Gray \n14 Cedar Ridge"
secondString = "Benjamin Gray 14 Cedar Ridge"
print(firstString)
print(secondString)

# Question 3
# Assume you have two variables: s="s" and p="p". Using concatenation and repetition, write an expression that produces the string Mississippi.

s = "s"
p = "p"
M = "Mi" + s*2 +"i" + s*2 + "i" + p*2 + "i"
print(M)
