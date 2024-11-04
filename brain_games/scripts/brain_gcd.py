from random import randint
from math import gcd
from brain_games.scripts import brain_games_main


def main():
    name = brain_games_main.main()
    print('Find the greatest common divisor of given numbers.')
    wins = 0

    while wins != 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        answer = gcd(first_number, second_number)
        print(f'Question: {first_number} {second_number}')

        try:
            ans = input('Your answer: ')
            int_user_answer = int(ans)
        except ValueError:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return

        if int_user_answer == answer:
            print('Correct!')
            wins += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
