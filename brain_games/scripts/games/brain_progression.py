from random import randint, choice
from brain_games.scripts.game_logic import start_text, check_logic


def main():
    text = 'What number is missing in the progression?'
    name, wins = start_text(text)

    while wins != 3:
        number = randint(1, 20)
        progression_len = randint(5, 15)
        modifier = randint(1, 10)
        progression = []

        for i in range(progression_len):
            progression.append(number)
            number += modifier

        answer_index = progression.index(choice(progression))
        answer = progression[answer_index]
        progression[answer_index] = '..'
        progression = [str(value) for value in progression]

        print(f"Question: {' '.join(progression)}")

        if not check_logic(answer, name):
            return
        else:
            wins += 1

    print(f'Congratulations, {name}!')
