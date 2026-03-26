import random


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def convert_fahrenheit_to_celsius(fahrenheit):
    assert fahrenheit >= -459.67
    return multiply(subtract(fahrenheit, 32), 5 / 9)


def roll_dice(n=5):
    return [random.randint(1, 6) for _ in range(n)]


def yahtzee():
    dice = roll_dice()
    for _ in range(2):
        counts = {x:dice.count(x) for x in set(dice)}
        keep_value = max(counts, key=counts.get)
        dice = [x for x in dice if x == keep_value]
        dice += [random.randint(1, 6) for _ in range(5 - len(dice))]
    return len(set(dice)) == 1