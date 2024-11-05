from random import randint
from brain_games.scripts.game_logic import start_text


def main():
    text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name, wins = start_text(text)

    while wins != 3:
        number = randint(2, 100)
        counter = 0
        print(f'Question: {number}')
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                counter += 1

        if counter == 0 or number == 2:
            ans = 'yes'
        else:
            ans = 'no'

        us_ans = input('Your answer: ')

        if us_ans == ans:
            print('Correct!')
            wins += 1
        else:
            print(f"'{us_ans}' is wrong answer ;(. Correct answer was '{ans}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
