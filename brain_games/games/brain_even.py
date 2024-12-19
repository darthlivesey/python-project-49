from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    number = randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'
    return answer, number


def is_even(number):
    return number % 2 == 0
