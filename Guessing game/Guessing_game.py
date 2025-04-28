#james Tademy
#CIS261
#Guessing game



import random

def play_game():
     upper_limit = int(input("Enter the highest number to guess: "))
    number = random.randint(1, upper_limit)
    print(f"I'm thinking of a number between 1 and {upper_limit}.")
   
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
