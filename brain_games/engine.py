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
            print('Correct!' )
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{current_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

    
    
