import prompt


def game_cycle(text, function):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(text)

    for _ in range(3):
        answer, question = function()
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
