#james Tademy
#CIS261
#Guessing game



import random

def play_game():
    number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")
   
    guess = int(input("Guess the number: "))
   
    while guess != number:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
       
        guess = int(input("Guess again: "))
   
    print("You got it!")

# Main loop to play again or quit
play_again = "yes"
while play_again == "yes":
    play_game()  # Call the function to play a round of the game
    play_again = input("Do you want to play again? (yes or no): ")

print("Thanks for playing! Goodbye!")
