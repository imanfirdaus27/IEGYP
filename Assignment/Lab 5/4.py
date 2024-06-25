# iman code
# {Rock; Paper} Paper (covering rock) wins, receiving a penny from rock.
# {Paper; Scissors} Scissors (cutting paper) wins, receiving a penny from paper.
# {Scissors; Rock} Rock (crushing scissors) wins, receiving a penny from scissors.

import random

def rockpaperscissors(a):
    
    b = random.randint(1,3)

    if b == 1:
        print("Computer's choice is rock")
    elif b == 2:
        print("Computer's choice is Paper")
    elif b == 3:
        print("Computer's choice is Scissors")

    if a == b:
        print("Tie!")
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("Congratulations! You win!")
    else:
        print("Computer wins!")
    
print("1. Rock")
print("2. Paper")
print("3. Scissors")
a = int(input("Please enter your choice:"))
rockpaperscissors(a)

# # chatgpt code
# import random

# def rock_paper_scissors():
#     print("Welcome to Rock, Paper, Scissors!")
#     print("Enter your choice:")
#     print("1. Rock")
#     print("2. Paper")
#     print("3. Scissors")
    
#     # Get user's choice
#     user_choice = int(input("Enter your choice (1-3): "))
    
#     # Validate user's choice
#     if user_choice < 1 or user_choice > 3:
#         print("Invalid choice. Please enter a number between 1 and 3.")
#         return
    
#     # Map user's choice to corresponding string
#     choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
#     user_choice_str = choices[user_choice]
    
#     # Generate computer's choice
#     computer_choice = random.randint(1, 3)
#     computer_choice_str = choices[computer_choice]
    
#     # Determine the winner
#     if user_choice == computer_choice:
#         print(f"Both players chose {user_choice_str}. It's a tie!")
#     elif (user_choice == 1 and computer_choice == 3) or \
#          (user_choice == 2 and computer_choice == 1) or \
#          (user_choice == 3 and computer_choice == 2):
#         print(f"You chose {user_choice_str} and computer chose {computer_choice_str}. You win!")
#     else:
#         print(f"You chose {user_choice_str} and computer chose {computer_choice_str}. Computer wins!")

# # Call the function to start the game
# rock_paper_scissors()
