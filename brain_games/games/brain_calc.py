from random import randint, choice


TEXT = 'What is the result of the expression?'


def brain_calc_logic():
    operation = choice(['+', '-', '*'])
    first_number = randint(1, 100)
    second_number = randint(1, 100)

    if operation == '-':
        answer = first_number - second_number
    elif operation == '+':
        answer = first_number + second_number
    elif operation == '*':
        answer = first_number * second_number

    question = f'{first_number} {operation} {second_number}'
    return answer, question
