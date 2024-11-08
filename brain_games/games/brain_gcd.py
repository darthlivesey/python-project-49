from random import randint
from math import gcd
from brain_games.scripts.game_logic import game_cycle


def main():
    text = 'Find the greatest common divisor of given numbers.'
    game_cycle(text, brain_gcd_logic)


def brain_gcd_logic():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    answer = gcd(first_number, second_number)
    print(f'Question: {first_number} {second_number}')
    return answer
