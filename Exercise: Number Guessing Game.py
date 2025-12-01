

#the number that the user has to guess
number = 9

# the question that the code is user inputing in and if the user is correct it will return Well guesses!
while True:
    guess = int(input("Guess a number 1-9: "))
    if guess == number:
        print("Well guessed!")
        