""" Maybe you already guessed it, but this is hangman """

import os
import time
import random

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def final_animation():
    x, d, d2 = 0, 1, 1
    opt = [1, 7]
    output = ''
    while True:
        if x == opt[d2]:
            d2 = 1 - d2
            d = d * -1
        x += d

        for z in range(x):
            output += hmanlist[z]

        print(output)
        output = ''

        time.sleep(.1)
        clear()

def printResults():
    print(f'Match: {m}/{len(guess_string)} \t {hman}')
    output = ''
    for x in w:
        output += f'{x} '
    return output

def vs_computer():
    words = ["helicopter", "netherlands", "easteregg", "skyscraper", "igor", "fero", "speaker",
                "bottle", "birthday", "sofa", "dryer", "facepalm", "freestyle", "weed", "smartphone",
                "dumbguy", "rotterdam", "bratislava", "debil", "kohut", "kokotleba"]
    clear()
    return words[random.randint(0, len(words))]

def vs_friend():
    # Enter a word to guess
    while True:
        guess = input('Enter a word to guess: ').lower()
        # For now only 1 word allowed
        if guess.isalpha() and len(guess) > 1:
            clear()
            return guess
        else:
            print('Enter one word, not a letter or a number!')

# Intro
guess_string = ''

while True:
    print('Choose game mode.')
    game_mode = int(input('1) vs computer\n2) vs friend\n... '))
    
    if game_mode == 1:
        guess_string = vs_computer()
        break
    elif game_mode == 2:
        guess_string = vs_friend()
        break
    else:
        print('Invalid input.')

temp_m, m, f = 0, 0, 0 
w, w2 = list(guess_string), []
hmanlist = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
hman = ''

# Fill in w2 dictionary with letters and indexes
for i in range(len(w)):
    if w[i] != ' ':
        w2.append({ "index": i, "letter": w[i] })
        w[i] = '_'
    else:
        w[i] = ' '

print(printResults())

while True:
    i = input('Guess a letter: ')

    if i.isalpha() and len(i) == 1:
        for x in range(len(w2)):
            if i == w2[x]['letter']:
                if w[w2[x]['index']] != i:
                    w[w2[x]['index']] = i
                    temp_m += 1

        # Guessed wrong
        if temp_m == m:
            if f >= len(hmanlist)-1:
                final_animation()
                # end
            else:
                hman += hmanlist[f]
                f += 1

        # Guessed right
        else:
            m = temp_m
            if m >= len(w2):
                clear()
                print(printResults())
                print('YOU WON!!!')
                break

        # Print results
        clear()
        print(printResults())

    else:
        print('Enter a letter, not a word or a number!')