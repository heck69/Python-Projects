import random

words = """engagement
railroad
white
precedent
horror
rugby
timetable
assume
rent
important
cutting
content
wardrobe
detector
foster
annual
echo
twitch
patient
offspring"""

words = words.split()

word = random.choice(words).lower()

if __name__ == '__main__':
    print('Guess the word! HINT: word is a fruit.')
    
    for _ in word:
        print('_', end=' ')
        
    
    while True:
        guess = input("Guess word:").lower()
        
        letterGuessed = ""
        
        if not guess.isalpha():
            print('Enter only a letter!')
            continue
        elif len(guess) > 1:
            print('Enter only a single letter!')
            continue
        elif guess in letterGuessed:
            print('You already guessed that letter!')
            continue
        if guess in word:
            letterGuessed += guess* word.count(guess)
        
        for char in word:
            if char in letterGuessed:
                print(char, end=' ')
            else:
                print('_', end=' ')

