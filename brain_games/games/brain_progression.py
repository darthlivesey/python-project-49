from random import randint, choice
from brain_games.game_logic import game_cycle


def main():
    text = 'What number is missing in the progression?'
    game_cycle(text, brain_progression_logic)


def brain_progression_logic():
    number = randint(1, 20)
    progression_len = randint(5, 15)
    modifier = randint(1, 10)
    progression = []

    for _ in range(progression_len):
        progression.append(number)
        number += modifier

    answer_index = progression.index(choice(progression))
    answer = progression[answer_index]
    progression[answer_index] = '..'
    progression = [str(value) for value in progression]

    question = ' '.join(progression)
    return answer, question
