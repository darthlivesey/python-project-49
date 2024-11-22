from random import randint


TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_prime_logic():
    question_number = randint(2, 100)
    return is_prime(question_number), question_number


def is_prime(question_number):
    counter = 0

    for i in range(2, (question_number // 2) + 1):
        if question_number % i == 0:
            counter += 1

    if counter == 0 or question_number == 2:
        answer = 'yes'
    else:
        answer = 'no'

    return answer
