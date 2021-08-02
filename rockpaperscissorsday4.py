rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer_line = "\nComputer chose:"

win_status = ["\nYou win", "\nYou draw", "\nYou lose"]

import random

computer_choice = random.randint(0, 2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if player_choice >= 3 or player_choice < 0:
  print("You chose an invalid number, you lose!")
else:
    if player_choice == 0:
      print(rock + computer_line)
      if computer_choice == 0:
        print(rock + win_status[1])
      elif computer_choice == 1:
        print(paper + win_status[2])
      else:
        print(scissors + win_status[0])
    elif player_choice == 1:
      print(paper + computer_line)
      if computer_choice == 0:
        print(rock + win_status[0])
      elif computer_choice == 1:
        print(paper + win_status[1])
      else:
        print(scissors + win_status[2])
    else:
      print(scissors + computer_line)
      if computer_choice == 0:
        print(rock + win_status[2])
      elif computer_choice == 1:
        print(paper + win_status[0])
      else:
        print(scissors + win_status[1])

