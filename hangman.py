""" Maybe you already guessed it, but this is hangman """

import os
import time

def clear():
    if os.name is 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printResults():
    print(f'Match: {m}/{len(guess)} \t {hman}')
    output = ''
    for x in w:
        output += f'{x} '
    return output

def animation():
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
        time.sleep(.200)
        clear()    

# Enter a word to guess
while True:
    guess = input('Enter a word to guess: ').lower()
    # For now only 1 word allowed
    if guess.isalpha() and len(guess) > 1:
        clear()
        break
    else:
        print('Enter one word, not a letter or a number!')

temp_m, m, f = 0, 0, 0
w = list(guess)
w2 = []
hmanlist = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
hman = ''

# Fill in w2 dictionary with letters and indexes
for i in range(len(w)):
    if w[i] is not ' ':
        w2.append({ "index": i, "letter": w[i] })
        w[i] = '_'
    else:
        w[i] = ' '

print(printResults())

while True:
    i = input('Guess a letter: ')

    if i.isalpha() and len(i) is 1:
        for x in range(len(w2)):
            if i is w2[x]['letter']:
                if w[w2[x]['index']] is not i:
                    w[w2[x]['index']] = i
                    temp_m += 1

        # Guessed wrong
        if temp_m is m:
            if f >= len(hmanlist)-1:
                animation()
                input()
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