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

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



#rock : 0, paper : 1, scissors : 2
ascii_images = [rock, paper, scissors]

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(ascii_images[userInput])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(ascii_images[computer_choice])


if userInput >=3 or userInput < 0:
  print("You typed an invaliusd number, you lose!")
elif userInput == 0 and computer_choice == 2:
  print("You win!")
elif userInput == 2 and computer_choice == 0:
    print("You lose!")    
elif computer_choice>userInput:
     print("You lose!")
elif userInput>computer_choice:
     print("You win!")
elif computer_choice == userInput:
    print("It's a tie!")
     
