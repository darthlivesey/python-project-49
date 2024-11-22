from random import randint


TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_logic():
    question_number = randint(1, 100)
    answer = 'yes' if question_number % 2 == 0 else 'no'
    return answer, question_number
