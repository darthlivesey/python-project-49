import prompt

WINS = 3


def run(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.GAME_DESCRIPTION)

    for _ in range(WINS):
        answer, question = game_module.generate_game_data()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if str(user_answer) == str(answer):
            print('Correct!')

        else:
            print(f"'{user_answer}' is wrong answer ;(.\
Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
