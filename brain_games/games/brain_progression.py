from random import randint

GAME_DESCRIPTION = 'What number is missing\
 in the progression?'


def generate_game_data():
    start = randint(0, 20)
    modifier = randint(1, 10)
    stop = randint(start + modifier * 5, start + modifier * 10)
    progression = list(range(start, stop, modifier))
    answer_index = randint(0, len(progression) - 1)
    answer = progression[answer_index]
    progression[answer_index] = '..'
    progression = [str(value) for value in progression]

    question = ' '.join(progression)
    return answer, question
