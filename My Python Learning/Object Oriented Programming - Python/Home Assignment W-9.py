# Created by Benjamin Gray 06/29/2021

# Q1. Evaluate the following statements by using "Sort"
# H = [4,5,3,9,1,6,7]
# What is the value of H when you are done?

H = [4, 5, 3, 9, 1, 6, 7 ]
H.sort()
print(H)

#Q2. Given the list of words ['the', 'quick', 'brown', 'fox'] use the
#"join" method on the following separator strings: " ", ':', ",", "--".

words = ['the', 'quick', 'brown', 'fox']
print(" ".join(words))
print(":".join(words))
print(",".join(words))
print("--".join(words))