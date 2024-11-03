from random import randint, choice
from brain_games.scripts import brain_games_main


def main():
    name = brain_games_main.main()
    print('What is the result of the expression?')
    wins = 0
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

        try:
            ans = input('Your answer: ')
            int_user_answer = int(ans)
        except ValueError:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return

        if int_user_answer == answer:
            print(f'Congratulations, {name}!')
            wins += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
