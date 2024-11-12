from random import randint
from brain_games.game_logic import game_cycle


def main():
    text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_cycle(text, brain_prime_logic)


def brain_prime_logic():
    question_number = randint(2, 100)
    counter = 0

    for i in range(2, (question_number // 2) + 1):
        if question_number % i == 0:
            counter += 1

    if counter == 0 or question_number == 2:
        answer = 'yes'
    else:
        answer = 'no'

    return answer, question_number
