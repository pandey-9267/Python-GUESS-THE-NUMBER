# SET OF INSTRUCTIONS OF THE GAME 

# Step-by-Step Instructions (the number range is form {1 - 100})

# • Choose the Secret Number: 
# You (the human player) think of a secret number and keep it to yourself. For example, let's say your secret number is 30.

# • The Computer Guesses: 
# The computer will generate a random guess. Let's say the computer guesses 50.

# • Give Feedback: 
#    Compare the computer's guess to your secret number:
# 	• If the computer's guess is too high (like 50 vs 30), you must tell the computer to guess a lower number.
# 	• If the computer's guess is too low, you must tell the computer to guess a higher number.

# • Win the Game: 
# The computer will keep adjusting its guesses based on your feedback until it correctly guesses your exact number.

import random

# Generate a random target between 1 and 100
target = random.randint(1, 100)

# Count the number of valid guesses
attempts = 0

while True:
    # Take input as a string so the user can enter Q to quit
    userChoice = input("Guess the target or Quit (Q): ")

    # Quit the game if the user enters Q or q
    if userChoice.upper() == "Q":
        break

    # Convert the input string into an integer
    userChoice = int(userChoice)

    # Check whether the guess is within the range
    if userChoice < 1 or userChoice > 100:
        print("You are out of range! Enter a number from 1 to 100.")
        continue  # Skip this guess and start the next loop

    # Increase the attempt counter
    attempts += 1

    # Check whether the guess is correct
    if target == userChoice:
        print("Congratulations! Correct Guess!")
        print(f"You guessed the number in {attempts} attempts.")
        break  # End the game after a correct guess

    # Tell the user if the guess is too small
    elif target > userChoice:
        print("Your number is too small. Take a bigger guess...")

    # Otherwise, the guess is too big
    else:
        print("Your number is too big. Take a smaller guess...")

# Display the game-over message after the loop ends
print("----GAME OVER----")
