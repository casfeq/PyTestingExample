import random
from functions import roll_dice, yahtzee
from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c
from functions import fizzbuzz
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add("space", "ship") == "spaceship"


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, -3) == -6
    assert multiply('ha', 3) == 'hahaha'


def test_subtract():
   assert subtract(3, 2) == 1


def test_convert_fahrenheit_to_celsius():
   assert f2c(32) == 0
   assert f2c(122) == pytest.approx(50)
   with pytest.raises(AssertionError):
       f2c(-600)


def test_roll_dice_with_fixed_seed():
    random.seed(12345)
    assert roll_dice() == [4, 6, 1, 3, 3]


def test_yahtzee_probability_smaller_sample():
    random.seed(12345)
    n = 20000
    successes = sum(yahtzee() for _ in range(n))
    p = successes/n
    assert 0.040 <= p <= 0.052


def test_yahtzee_probability():
    random.seed(12345)
    n = 100000
    successes = sum(yahtzee() for _ in range(n))
    p = successes/n
    assert 0.042 <= p <= 0.050
    
    
def test_fizzbuzz_multiples_of_three():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'


def test_fizzbuzz_multiples_of_five():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'


def test_fizzbuzz_multiples_of_three_and_five():
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'


def test_fizzbuzz_other_integers():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(7) == 7


def test_fizzbuzz_zero_raises():
    with pytest.raises(ValueError):
        fizzbuzz(0)


def test_fizzbuzz_negative_raises():
    with pytest.raises(ValueError):
        fizzbuzz(-1)
    with pytest.raises(ValueError):
        fizzbuzz(-15)


def test_fizzbuzz_non_integer_raises():
    with pytest.raises(TypeError):
        fizzbuzz(3.5)
    with pytest.raises(TypeError):
        fizzbuzz('3')
    with pytest.raises(TypeError):
        fizzbuzz(None)
