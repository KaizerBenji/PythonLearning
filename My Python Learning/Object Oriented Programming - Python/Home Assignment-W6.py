# Home Assignment-W6Home Assignment-W6
# Created by: Benjamin Gray
# You have been given the following lists of Color and their specific codes:
Colors = ['Red', 'Blue', 'Green', 'Black', 'Yellow', 'Orange', 'Purple', 'Nocolor']
Codes = [97, 17, 19, 128, 66, 111, 231, 00]
codeDict = dict()
# 1. Using codeDict, find the score for 'Nocolor'.
for key in Colors:
    for value in Codes:
        codeDict[key] = value
        Codes.remove(value)
        break
print(codeDict['Nocolor'])
# 2. Add a code of 333 for 'Nocolor'.
for key in Colors:
    for value in Codes:
        codeDict[key] = value
        Codes.remove(value)
        break
codeDict['Nocolor'] = 333
x = codeDict
print(x)
# 3. Create a sorted list of all the codes in codeDict.
for key in Colors:
    for value in Codes:
        codeDict[key] = value
        Codes.remove(value)
        break
values = list(codeDict.values())
values.sort()
print(values)
# 4. Update the name for 'Nocolor' to be ‘white’
for key in Colors:
    for value in Codes:
        codeDict[key] = value
        Codes.remove(value)
        break
for key in codeDict.keys():
    if key == 'Nocolor':
        codeDict['White'] = codeDict['Nocolor']
        del codeDict['Nocolor']
        break
print(codeDict)
# 5. White was not a part of original colors list so, just Delete it and its code from codeDict.
for key in Colors:
    for value in Codes:
        codeDict[key] = value
        Codes.remove(value)
        break
codeDict.popitem()
print(codeDict)
