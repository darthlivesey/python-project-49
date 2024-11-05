from random import randint
from brain_games.scripts.game_logic import start_text


def main():
    text = 'Answer "yes" if the number is even, otherwise answer "no".'
    name, wins = start_text(text)

    while wins != 3:
        question_number = randint(1, 100)
        print(f'Question: {question_number}')
        ans = input('Your answer: ')
        condition_1 = question_number % 2 == 0 and ans == 'yes'
        condition_2 = question_number % 2 != 0 and ans == 'no'

        if condition_1 or condition_2:
            print('Correct!')
            wins += 1
        else:
            _ = 'yes' if question_number % 2 == 0 else 'no'
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{_}'")
            print(f"Let's try again, {name}")
            return

    print(f'Congratulations, {name}!')
