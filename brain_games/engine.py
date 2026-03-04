import prompt

round = 3


def welcome_user(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.start_quest)
    for i in range(round):
        question, current_answer = game.game_start()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == current_answer:
            print('Correct!')
        else:
            q1 = f"'{answer}' is wrong answer ;(. "
            q2 = f"Correct answer was '{current_answer}'."
            print(f'{q1} + {q2}')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

    
    
