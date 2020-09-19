parrot = "Norwegian Blue"
#         012345678901234

print(parrot[0:6:2]) #slice start at position 0 up to position 6 but not including and in steps of 2
print(parrot[0:6:3]) #slice start at position 0 up to position 6 but not including and in steps of 3
print()

number = "9,223;372:036 854,775;807"
print(number[1::4]) #starts at position 1 and slices every 4th character
print()

seperators = number[1::4]
print(seperators)
print()

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val)for val in values])