from random import randint
from math import gcd
from brain_games.scripts.game_logic import start_text, check_logic


def main():
    text = 'Find the greatest common divisor of given numbers.'
    name, wins = start_text(text)

    while wins != 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        answer = gcd(first_number, second_number)
        print(f'Question: {first_number} {second_number}')

        if not check_logic(answer, name):
            return
        else:
            wins += 1

    print(f'Congratulations, {name}!')
