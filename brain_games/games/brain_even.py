from random import randint


def main():
    question_number = randint(1, 100)
    answer = 'yes' if is_even(question_number) else 'no'
    return answer, question_number


def is_even(question_number):
    if question_number % 2 == 0:
        return True
    else:
        return False


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
