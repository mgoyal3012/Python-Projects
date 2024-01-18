import random
stages=['''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
==========   
    ''','''
    +---+
    |   |
    0   |
   /|\  |
   /    |
==========
    ''','''
    +---+
    |   |
    0   |
   /|\  |
        |
==========
    ''','''
    +---+
    |   |
    0   |
   /|   |
        |
==========
    ''','''
    +---+
    |   |
    0   |
   /    |
        |
==========
    ''','''
    +---+
    |   |
    0   |
        |
        |
==========
    ''']
word_list=["aarushi","aashi","jasmine","gouri","meera"]
chosen_word=random.choice(word_list)
print(f"The solution is {chosen_word}")
display=[]
for _ in range(len(chosen_word)):
    display+="_"
end_of_game=False
lives=6
while end_of_game==False and lives>0:
    guess=input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives -= 1
        if lives==0:
            end_of_game=True
            print("You lose.")
    print(display)
    if "_" not in display:
        end_of_game=True
        print("You win.")
    print(stages[lives])