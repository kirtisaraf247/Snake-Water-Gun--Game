import random

cp = 0
up = 0
turn = 0
lst = ['s', 'w', 'g']
while turn < 10:
    cc = random.choice(lst)
    uc = input("Enter your choice:type \'s' for Snake, \'w' for Water and \'g' for Gun:\n")

    if cc == 's' and uc == 'w':
        print('Computer WON.')
        cp = +1
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 'g' and uc == 's':
        print('Computer WON.')
        cp = +1
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 'w' and uc == 'g':
        print('Computer WON.')
        cp = +1
        turn += 1
        print('Remaining turns=', 10 - turn)
    elif cc == 'w' and uc == 's':
        print('You WON.')
        up = +1
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 's' and uc == 'g':
        print('You WON.')
        up = +1
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 's' and uc == 'g':
        print('You WON.')
        up = +1
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 's' and uc == 's':
        print("It's a Draw")
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 'g' and uc == 'g':
        print("It's a Draw")
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue
    elif cc == 'w' and uc == 'w':
        print("It's a Draw")
        turn += 1
        print('Remaining turns=', 10 - turn)
        continue

if turn == 10:
    print('\nGAME OVER')
    if cp > up:
        print('\nComputer WON the game...')
    else:
        print('\nYayyy!!!\nYou WON the game...')
