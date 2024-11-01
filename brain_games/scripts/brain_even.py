from random import randint


def main(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins = 0


    while wins != 3:
        question_number = randint(1, 100)
        print(f'Question: {question_number}')
        answer = input('Your answer: ')
        if (question_number % 2 == 0 and answer == 'yes') or (question_number % 2 != 0 and answer == 'no'):
            print('Correct!')
            wins += 1
        else:
            print (f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if question_number % 2 == 0 else 'no'}'")
            print(f"Let's try again, {name}")
            return
    

    print(f'Congratulations, {name}!')
