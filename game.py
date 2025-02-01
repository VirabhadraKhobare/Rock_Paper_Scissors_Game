import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Rock: 0, Paper: 1, Scissors: 2
ascii_images = [rock, paper, scissors]

# User input validation
try:
    userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    if userInput not in [0, 1, 2]:
        print("Invalid choice! Please enter 0, 1, or 2.")
    else:
        print("You chose:")
        print(ascii_images[userInput])

        # Computer's choice
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(ascii_images[computer_choice])

        # Determine the winner
        if userInput == computer_choice:
            print("It's a tie!")
        elif (userInput == 0 and computer_choice == 2) or \
             (userInput == 1 and computer_choice == 0) or \
             (userInput == 2 and computer_choice == 1):
            print("You win! 🎉")
        else:
            print("You lose! 😢")

except ValueError:
    print("Invalid input! Please enter a number (0, 1, or 2).")
