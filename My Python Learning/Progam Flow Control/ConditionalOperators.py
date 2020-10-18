#less than <
#less than or equal to <=
#greater than >
#greater than or equal to >=
#equal to ==
#not equal to

answer = 5

print("Plz guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Plz guess higher!")
    else:
        print("Plz guess lower!")
    guess = int(input())
    if guess == answer:
        print("Well done! you guessed it!")
    else:
        print("Sorry! You guessed wrong!")
else:
    print("You guessed it the first time!")