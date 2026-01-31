import random
from hangmanlogo import logos
from wordslist  import medium_words
from hangmanstages import hangman_stages


choosenlogo= random.choice(logos)
print(choosenlogo)


wordslist = medium_words

lives = 6

choosed = random.choice(wordslist)

display = []

print(choosed)

for _ in range(len(choosed)):
    display += "_"
end_of_game = False

while not end_of_game:

    guessletter = input(" Please Guess a letter: ").lower()

    for position in range(len(choosed)):
        letter = choosed[position]
        if letter == guessletter:
            display[position] = letter

    if guessletter not in choosed:
         lives -= 1
         if lives == 0:
            end_of_game = True
            print("You Loose Your Person is Killed")    
    print(display)
    if "_" not in display:
            print("You Won, You Saved a life")
            end_of_game = True
    
    print(hangman_stages[lives])