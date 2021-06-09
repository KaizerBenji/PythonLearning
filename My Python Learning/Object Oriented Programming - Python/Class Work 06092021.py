# You have been given the following lists of Grad students and their final exam scores:
Students = ["Kalra", "Malik", "John", "Ajay", "Vijay", "Anwar", "Ali", "Jose", "Hector", "Noname"]
Scores = [70, 65, 80, 75, 60, 55, 85, 83, 77, 0]
# 1. Using scoreDict, find the score for 'Noname'.
scoreDict = dict()
for key in Students:
    for value in Scores:
        scoreDict[key] = value
        Scores.remove(value)
        break
print(scoreDict["Noname"])

# 2. Add a score of 100 for 'Noname'.
for key in Students:
    for value in Scores:
        scoreDict[key] = value
        Scores.remove(value)
        break
scoreDict["Noname"] = 100
x = scoreDict
print(x)

# 3. Create a sorted list of all the scores in scoreDict.
for key in Students:
    for value in Scores:
        scoreDict[key] = value
        Scores.remove(value)
        break
values = list(scoreDict.values())
values.sort()
print(values)

# 4. Update the name for 'Noname' to be Professor Chak.
for key in Students:
    for value in Scores:
        scoreDict[key] = value
        Scores.remove(value)
        break
for key in scoreDict.keys():
    if key == "Noname":
        scoreDict["Prof. Chak"] = scoreDict["Noname"]
        del scoreDict["Noname"]
        break
print(scoreDict)

# 5. Professor Chak is not a student so, just Delete him and his score from scoreDict.
for key in Students:
    for value in Scores:
        scoreDict[key] = value
        Scores.remove(value)
        break
for key in scoreDict.keys():
    if key == "Noname":
        scoreDict["Prof. Chak"] = scoreDict["Noname"]
        del scoreDict["Noname"]
        break
del scoreDict["Prof. Chak"]
print(scoreDict)
