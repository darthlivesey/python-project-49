from random import randint
from brain_games.scripts import brain_games_main


def main():
    name = brain_games_main.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins = 0

    while wins != 3:
        question_number = randint(1, 100)
        print(f'Question: {question_number}')
        answer = input('Your answer: ')
        condition_1 = question_number % 2 == 0 and answer == 'yes'
        condition_2 = question_number % 2 != 0 and answer == 'no'
        if condition_1 or condition_2:
            print('Correct!')
            wins += 1
        else:
            _ = 'yes' if question_number % 2 == 0 else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{_}'")
            print(f"Let's try again, {name}")
            return

    print(f'Congratulations, {name}!')
