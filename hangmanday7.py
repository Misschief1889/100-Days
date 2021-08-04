
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(f'Pssst, the solution is {chosen_word}.')

lives = 6


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    print("".join(display))

    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter
    if guess not in chosen_word:
      lives -= 1


    print(stages[lives])
    
    if lives == 0:
        end_of_game = True
        print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print("".join(display))

