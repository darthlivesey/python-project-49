from random import randint


GAME_DESCRIPTION = 'Answer "yes" if given number is prime.\
Otherwise answer "no".'


def main():
    question_number = randint(2, 100)
    answer = 'yes' if is_prime(question_number) else 'no'
    return answer, question_number


def is_prime(question_number):
    counter = 0

    for i in range(2, (question_number // 2) + 1):
        if question_number % i == 0:
            counter += 1

    if counter == 0 or question_number == 2:
        return True
    else:
        return False
