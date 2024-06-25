# iman code
import random

def numberguessinggame(a):
    
    b = random.randint(1,100)
    print(f"random number is {b}")

    if a<b:
        print("Your number is too low")
    elif a>b:
        print("Your number is too high")
    elif a==b:
        print("Congratulations! You guess the correct number")

a = int(input("Please enter your guess number (between 1 - 100):"))
numberguessinggame(a)

# # chatgpt code
# import random

# def guess_number_game():
#     # Generate a random number between 1 and 100
#     secret_number = random.randint(1, 100)
    
#     print("Welcome to the Number Guessing Game!")
#     print("I have chosen a number between 1 and 100. Can you guess what it is?")
    
#     while True:
#         # Prompt the user to guess the number
#         user_guess = int(input("Enter your guess (between 1 and 100): "))
        
#         # Compare the user's guess with the secret number
#         if user_guess < secret_number:
#             print("Too low! Try again.")
#         elif user_guess > secret_number:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You guessed the correct number, which is {secret_number}.")
#             break

# # Call the function to start the game
# guess_number_game()