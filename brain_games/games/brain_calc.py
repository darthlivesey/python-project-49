from random import randint, choice
from brain_games.scripts.game_logic import game_cycle


def main():
    text = 'What is the result of the expression?'
    game_cycle(text, brain_calc_logic)


def brain_calc_logic():
    operation = choice(['+', '-', '*'])
    first_number = randint(1, 100)

    if operation == '-':
        second_number = randint(1, 99)
        while second_number > first_number:
            second_number = randint(1, 99)
        answer = first_number - second_number
    elif operation == '+':
        second_number = randint(1, 100)
        answer = first_number + second_number
    elif operation == '*':
        second_number = randint(1, 20)
        answer = first_number * second_number

    print(f'Question: {first_number} {operation} {second_number}')

    return answer
