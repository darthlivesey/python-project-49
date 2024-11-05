from brain_games.scripts.brain_games import main


def start_text(text):
    name = main()
    print(text)
    return name, 0


def check_logic(answer, name):
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
