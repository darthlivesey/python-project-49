from brain_games.scripts import brain_games_main


def start_text(text):
    name = brain_games_main.main(), 0
    print(text)
    return name

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