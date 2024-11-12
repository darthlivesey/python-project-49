import prompt


def game_cycle(text, function):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(text)

    for _ in range(3):
        a, question = function()
        print(f'Question: {question}')
        ua = input('Your answer: ')
        if str(ua) == str(a):
            print('Correct!')

        else:
            print(f"'{ua}' is wrong answer ;(. Correct answer was '{a}'")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
