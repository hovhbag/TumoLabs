import random

def dice():
    return random.choice([1,2,3,4,5,6])

def second_play(n):
    while True:
        l = {"dice1":dice(), "dice2":dice(), "goal":n}
        sum = l["dice1"] + l["dice2"]
        print(f"The sum of dice is {l['dice1']} + {l['dice2']} = {sum}")
        if sum == n:
            return "You won"
        elif sum == 7:
            return "You lose"

def start():
    l = {"dice1":dice(), "dice2":dice(), "casino":[2, 3, 12], "player":[7, 11], "other":[4, 5, 6, 8, 9, 10]}
    sum = l['dice1'] + l['dice2']
    print(f"The sum of dice is {l['dice1']} + {l['dice2']} = {sum}")
    if sum in l['casino']:
        return "You lose"
    elif sum in l['player']:
        return "You won"
    elif sum in l['other']:
        print(f'Now your goal number is {sum}')
        return second_play(sum)

if __name__ == '__main__':
    print(start())
