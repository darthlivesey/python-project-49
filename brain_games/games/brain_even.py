from random import randint
from brain_games.game_logic import game_cycle


def main():
    text = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_cycle(text, brain_even_logic)


def brain_even_logic():
    question_number = randint(1, 100)
    answer = 'yes' if question_number % 2 == 0 else 'no'
    return answer, question_number
