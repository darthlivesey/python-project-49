from random import randint

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'


def generate_game_data():
    number = randint(2, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return answer, number


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False

    return True
