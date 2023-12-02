import random
import hangman_stages
import word_file
lives=6
chosenword=random.choice(word_file.words)
print(chosenword)
display=[]
for i in range(len(chosenword)):
    display+='_'
print(display)
gameover=False
while not gameover:
    guessedletter=input("guess a letter:").lower()
    for position in range(len(chosenword)):
        letter=chosenword[position]
        if letter==guessedletter:
            display[position]=guessedletter
    print(display)
    if guessedletter not in chosenword:
        lives-=1
        if lives==0:
            gameover=True
            print("you lose!!")
        if '_' not in display:
            gameover=True
            print("you win!!")
        print(hangman_stages.stages[lives])
