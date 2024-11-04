from random import randint, choice
from brain_games.scripts.game_logic import start_text, check_logic


def main():
    text = 'What is the result of the expression?'
    name, wins = start_text(text)
    symbols_list = ['+', '-', '*']

    while wins != 3:
        operation = choice(symbols_list)
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

        if not check_logic(answer, name):
            return
        else:
            wins += 1

    print(f'Congratulations, {name}!')
