#print("C:\Users\timburbon\notes.txt") this string will cause errors because the /t is trying to tab and \n is trying to split
print("C:\\Users\\timburbon\\notes.txt") #the escpae char(\) can help clear up this issue
print(r"C:\Users\timburbon\notes.txt") #putting in the r creates a raw string, first method is preferred
