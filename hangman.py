import random

print("hello and welcome to Hangman")

wordlist = ["elephant", "lion" , "gazel" , "crocodile"]

Secret_Word = random.choice(wordlist)



display_word = []

for letter in Secret_Word:
    display_word += '_'
print(Secret_Word)
print(display_word)
num = 0
game_over = False
while not game_over:
    user_guess = str(input("guess the  letter you think is in the word: ")).lower()
    for position in range(len(Secret_Word)):
        letter = Secret_Word[position]
    if user_guess not in Secret_Word:
        num += 1
        guess_left = 5 - num
        print(f"you have {guess_left} left")
        if num >= 5:
            print("game over you lose")
            game_over = True


    print(display_word)
    if "_" not in display_word:
        print("you win")
        game_over = True

