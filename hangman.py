import random
from hangman_word_list import words
print(
"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      """)

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
list_of_words = words
word = random.choice(list_of_words)
blank = []
for _ in range(len(word)):
    blank += '_'
Blank = ' '.join(blank)
print("\nThe given blanks for the word is:",Blank)
lives = 6
goal = False
while not goal:
    guess_letter = input("Guess a letter: ")
    for i in range(len(word)):
        if word[i] == guess_letter:
            blank[i] = guess_letter
    print(f"{' '.join(blank)}")
    if guess_letter not in word:
        lives -= 1
        print(f"You have guessed the letter'{guess_letter}', this letter is not in the word. You Lose a life")
        if lives == 0:
            goal = False
            print("Better luck next time 😓. The word is:",word)
    print(stages[lives])
    if '_' not in blank:
        goal = True
        print("Yah!!!! You Win 😊.")       