def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def convert_fahrenheit_to_celsius(fahrenheit):
    assert fahrenheit >= -459.67
    return multiply(subtract(fahrenheit, 32), 5 / 9)


def fizzbuzz(n):
    if not isinstance(n,int):
        raise TypeError('Input must be integer')
    if n <= 0:
        raise ValueError('Input must be positive integer')
    if n%3 == 0 and n%5 == 0:
        return 'FizzBuzz'
    if n%3 == 0:
        return 'Fizz'
    if n%5 == 0:
        return 'Buzz'
    return n