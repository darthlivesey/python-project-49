from math import gcd
from random import randint


def main():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return answer, question


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
