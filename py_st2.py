import random

def dice():
    return random.choice([1,2,3,4,5,6])

def second_play(n):
    while True:
        l = [dice(), dice(), n]
        sum = l[0] + l[1]
        print(f"The sum of dice is {l[0]} + {l[1]} = {sum}")
        if sum == n:
            return "You won"
        elif sum == 7:
            return "You lose"

def start():
    l = [dice(), dice(), [2, 3, 12], [7, 11], [4, 5, 6, 8, 9, 10]]
    sum = l[0] + l[1]
    print(f"The sum of dice is {l[0]} + {l[1]} = {sum}")
    if sum in l[2]:
        return "You lose"
    elif sum in l[3]:
        return "You won"
    elif sum in l[4]:
        print(f'Now your goal number is {sum}')
        return second_play(sum)

if __name__ == '__main__':
    print(start())
