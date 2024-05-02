import random
stages = ["""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""", 
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""", 
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""", 
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", 
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""", 
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
 """
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

list_of_words = ["airline","blue","cotton","dandelion","elephant","flower","goat","human","india","japan","kenya","lemon","money","newyork","onion","penguin","quail","raise","structure","tabala","uppercase","venus","water","xylophone","yellow","zebra"]

random_word = random.choice(list_of_words)
word_length = len(random_word)
blank_pattern = ""
is_alive = True
lives = 6
for x in range(word_length):
  blank_pattern += "_ "
print(f"YOUR WORD IS {len(random_word)} LETTERS:\n {blank_pattern}")

display = []
for i in random_word:
    display+= "_"
while is_alive:
  guess = input("GUESS A LETTER : ").lower()
  if guess in display:
    print("You have already guessed the letter")
  for i in range(word_length):
    check_letter = random_word[i]
    if check_letter == guess:
      display[i] = guess
    else:
      pass
  print(f"{' '.join(display)}\t\t")

  if "_" not in display:
    is_alive = False
    print("YOU WON")
  if guess not in display:
    lives -=1
    if lives == 6:
      print(stages[6])
    elif lives == 5:
      print(stages[5])
    elif lives == 4:
      print(stages[4])
    elif lives == 3:
      print(stages[3])
    elif lives == 2:
      print(stages[2])
    elif lives == 1:
      print(stages[1])
    else:
      print(stages[0])
      is_alive = False
      print("YOU LOST")
      print(f"Your word was:{random_word}")