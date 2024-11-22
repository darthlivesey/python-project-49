from random import randint
from math import gcd


TEXT = 'Find the greatest common divisor of given numbers.'


def brain_gcd_logic():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return answer, question
