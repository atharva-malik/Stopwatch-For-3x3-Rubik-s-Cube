import datetime
import random

moves = ["F", "B", "U", "D", "L", "R"]
direction = ["'", "2", ""]
length = random.randrange(20, 26)


def scramble_gen():
    scramble = [0] * length
    for i in range(len(scramble)):
        scramble[i] = [0] * 2
    return scramble


def scramble_replace(scramble):
    for i in range(len(scramble)):
        scramble[i][0] = random.choice(moves)
        scramble[i][1] = random.choice(direction)
    return scramble


def valid(scramble):
    for i in range(1, len(scramble)):
        while scramble[i][0] == scramble[i - 1][0]:
            scramble[i][0] = random.choice(moves)
    for i in range(2, len(scramble)):
        while scramble[i][0] == scramble[i - 2][0] or scramble[i][0] == scramble[i - 1][0]:
            scramble[i][0] = random.choice(moves)
    return scramble


def join(scramble):
    final = []
    for i in range(len(scramble)):
        final.append(str(scramble[i][0]) + str(scramble[i][1]))
    text = "  ".join(final)
    return text


def call():
    s = scramble_replace(scramble_gen())
    scramble = join(valid(s))
    return scramble


while True:
    random_jumble = call()
    print(random_jumble)
    a = input("Press 'e' and enter to end the program\n")
    if a != 'e':
        startTime = datetime.datetime.now()
        input("")
        finaltime = datetime.datetime.now() - startTime
        print("Your Time is: " + str(finaltime))
    else:
        break
