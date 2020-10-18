answer = 5

print("Plz guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Plz guess higher!")
    guess = int(input())
    if guess == answer: #two == is testing for equality
        print("Well done, you guessed it!")
    else:
        print("Sorry, you guessed wrong!")
elif guess > answer:
    print("Plz guess lower!")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you guessed wrong!")
else:
    print("You got it right the first time!")