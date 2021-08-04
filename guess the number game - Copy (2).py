#a game where the player tries to guess what number the computer is thinking of between 1 and 20
import random

def guessingGame():
    guessesTaken = 0

    print ("Hey there! What's your name? ")
    myName = input()

    number = random.randint (1, 20)

    print ("Well there " + myName +', ' "I am thinking of a number between 1 and 20 what is it?")

    for guessesTaken in range(6):
        print ('Take a guess')
        guess = input()
        guess = int(guess)

        if guess < number:
            print ("Your guess is too low")

        if guess > number:
            print("Your guess is too high")

        if guess == number:
            break

    if guess == number:
        print ("Good job " + myName + "! you correctly guessed the number I was thinking of in " + str(guessesTaken) + " Tries!")

    if guess != number:
        print ("Too bad, my number was " + str(number))

guessingGame()
