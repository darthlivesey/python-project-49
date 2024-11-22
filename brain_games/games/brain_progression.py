from random import randint, choice


TEXT = 'What number is missing in the progression?'


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
