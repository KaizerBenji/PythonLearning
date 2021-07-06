# Created by Benjamin Gray
# Midterm Practical
names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]
scoreDict = dict()
for key in names:
    for value in scores:
        scoreDict[key] = value
        scores.remove(value)
        break
# Using scoreDict, find the score for 'barb'
print(scoreDict["barb"])
# Add a score of 19 for 'john'
scoreDict["john"] = 19
x = scoreDict
print(x)
# Create a sorted list of all the scores in scoreDict.
values = list(scoreDict.values())
values.sort()
print(values)
# Calculate the average of all the scores in scoreDict.
avg = sum(scoreDict.values()) / len(scoreDict.values())
print(avg)
# Update the score for 'sally' to be 13.
scoreDict['sally'] = 13
print(x)
# Tom has just dropped this class. Delete 'tom' and his score from scoreDict.
scoreDict.pop("tom")
print(x)