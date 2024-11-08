import prompt


def start_text(text):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(text)
    return name


def check_int_logic(answer, name):
    try:
        ans = input('Your answer: ')
        int_user_answer = int(ans)
    except ValueError:
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'")
        print(f"Let's try again, {name}!")
        return False

    if int_user_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'")
        print(f"Let's try again, {name}!")
        return False


def check_str_logic(user_answer, answer, name):
    ua = user_answer
    a = answer

    if user_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{ua}' is wrong answer ;(. Correct answer was '{a}'")
        print(f"Let's try again, {name}!")
        return False


def game_cycle(text, function, option=0):
    name = start_text(text)
    wins = 0

    while wins != 3:
        if option == 1:
            answer, question_number = function()
            print(f'Question: {question_number}')
            user_answer = input('Your answer: ')
            if check_str_logic(user_answer, answer, name):
                wins += 1
            else:
                return
        else:
            answer = function()
            if check_int_logic(answer, name):
                wins += 1
            else:
                return

    print(f'Congratulations, {name}!')
