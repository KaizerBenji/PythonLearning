parrot = "Norwegian Blue"
#         012345678901234
print(parrot[0:6]) #telling python to slice starting at postion 0 and up to position 6 but not including it in the slice
print()

print(parrot[3:5]) #starting at position 3 and up to but not including position 5
print()

print(parrot[0:9])
print(parrot[:9]) #the start value will default to the start of the sequence if no start value is given
print()

print(parrot[10:14])
print(parrot[10:]) #if there is not stop value then the sequence will end at the last value of the string
print()

print(parrot[:6] + parrot[6:])
print()

print(parrot[:]) #with no start or stop then the whole string will be printed