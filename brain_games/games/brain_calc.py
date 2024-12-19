from random import choice, randint


def main():
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


GAME_DESCRIPTION = 'What is the result of the expression?'
