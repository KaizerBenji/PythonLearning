splitString = "This string has been \nsplit over \nseveral lines" # \n is used to split strings onto different lines
print(splitString)

tabbedString = "1\t2\t3\t4\t5" #\t is used to tab in a string
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting."') #need to use the escape char (\)  before the ' inside the string
#or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting.\"") #use the escape char (\) before and after the quote within the string
#or
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""") #when using triple quotes you do not need an escape char(\) it knows that the string does not end till the second use of triple quotes

anotherSplitString = """This line will 
be split
over several 
lines"""
print(anotherSplitString) #the triple quotes allows you to split over several lines without the \n

notSplit = """This string will \
not be split \
over several lines"""
print(notSplit) #using the escape cahr (\) with the triple quotes so the string will not be split over the lines