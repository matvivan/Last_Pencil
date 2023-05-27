from random import randint

    
def random_name():
    cons = ['th', 'sh', 'ch', 'ph', 'sk', 'st', 'tr', 'br', 'gr', 'cl', 'hn',
        'w','r','t','p','s','d','f','g','h','j','k','l','z','c','v','b','n','m']
    vowl = ["ee", "ea", "ai", "ia", "ou", "au", "io", "oe", "ei", "ui", 
        'a','e','u','i','o']

    name = ''
    for syllable in range(randint(1, 3)):
        name += cons[randint(0, 28)]
        name += vowl[randint(0, 14)]

    return name.title()


def read_initial_pencils():
    while True:
        x = input()
        if not x.isdigit():
            print("The number of pencils should be numeric")
        elif x == '0':
            print("The number of pencils should be positive")
        else:
            break
    return int(x)


def read_first_player(names):
    while True:
        try:
            first = input()
            i = names.index(first)
            break
        except ValueError:
            print("Choose between '{}' and '{}'".format(*names))
    return i


def read_correct_turn(num):
    while True:
        x = input()
        if x not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
        elif int(x) > num:
            print("Too many pencils were taken")
        else:
            break
    return int(x)
    

def compute_bot_turn(num):
    return [3, 1, 1, 2][num % 4]


# read initial number of pencils
print('How many pencils would you like to use:')
pencils = read_initial_pencils()

# read first player until correct name typed
names = (random_name(), random_name())
print("Who will be the first ({}, {}):".format(*names))
i = read_first_player(names)

# start the game
while pencils > 0:
    
    # show pencils and whose turn
    print('|' * pencils)
    print(f"{ names[i] }'s turn!")

    # read player's or bot's turn and discard pencils
    if i == 1:
        x = compute_bot_turn(pencils)
        print(x)
    else:
        x = read_correct_turn(pencils)
    pencils -= x
    
    # switch turn
    i ^= 1
    
# announce the winner
print(names[i], "won!")
