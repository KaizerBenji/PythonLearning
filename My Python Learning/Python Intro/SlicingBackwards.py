letters = "abcdefghijklmnopqrstuvwxyz"
#          12345567890123456789012345
backwards = letters[25::-1] #you may also omit the start value, [::-1]this is a python idiom called reversing the sequence
print(backwards)
print()

print(letters[16:13:-1]) #slice qpo
print(letters[4::-1]) #slice edcba
print(letters[:-9:-1]) #slice the last 8 char in reverse order
print(letters[-4:]) #if the start value you is a negative, it will begin at the end of a string
print(letters[-1:])
print(letters[:1]) #will pull the first char of the string
print(letters[0]) #will pull the first char of the string