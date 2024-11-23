import random

def getRandomNum():
    # Generate a random number between 1 and 100
    return random.randint(1, 100)

def checkChoice():
    randomNum = getRandomNum()  # Generate the random number
    print("Guess the number (between 1 and 100):")

    while True:  # Start a loop to keep the game running
            # Take user input
            numInput = float(input("Enter your guess: "))

            # Check the guess
            if numInput == randomNum:
                print("You Won!")
                print("Generating a new number...\n")
                randomNum = getRandomNum()  # Generate a new number for the next round
            elif numInput > randomNum:
                print("Pick a lower number.")
            elif numInput < randomNum:
                print("Pick a higher number.")

# Start the game
checkChoice()
