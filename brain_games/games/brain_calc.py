from random import randint, choice
from brain_games.game_logic import game_cycle


def main():
    text = 'What is the result of the expression?'
    game_cycle(text, brain_calc_logic)


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

    question_string = f'{first_number} {operation} {second_number}'
    return answer, question_string
