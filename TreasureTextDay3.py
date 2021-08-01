print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You come across a fork in the road. Do you go >left< or >right<?\n")
first_answer = input()
import sys
if first_answer == 'right':
  print("Oh, no! While turning right, you come across a swarm of angry bees. While running from them, you fall down a hole and die.\n \n Game over. :( ")
  sys.exit()
else:
  print("You travel down the path, and come to a dock out in the hot sun. You can see an island, off in the distance. Do you >swim<, or >wait< for a boat?\n")

second_answer = input()
if second_answer == 'swim':
  print("You decide waiting in the hot sun is for the birds! You leap off the dock and start swimming. It isn't long before you feel a pain, however, and then another- A hundred nibbles! You're eaten by trout while trying to reach the island.\n \n Game over. :( ")
  sys.exit()
else:
  print("You wait for the boat, and while it's a bit sweaty and slow you arrive on the island safely. Before you sits a hut. There are three doors: >red<, >blue<, and >yellow<. Which door do you pick?\n")

third_answer = input()
if third_answer == 'red':
  print("You open the door, and immediately there is a flaming explosion that burns you to ash right where you stand. You died.\n \n Game over. :( ")
  sys.exit()
elif third_answer == 'blue':
  print("You open the door, and immediately an elephant comes charging out, squashing you where you stood. You died.\n \n Game over. :( ")
  sys.exit()
else:
  print("Upon opening the door, you're greeted by... A massive, shimmering pile of gold! You did it!\n \n You win. :) ")
  sys.exit()

