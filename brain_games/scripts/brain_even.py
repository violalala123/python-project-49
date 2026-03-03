import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
  


    print('Answer "yes" if the number is even, otherwise answer "no".')
    current = 0
    while current < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        current_answer = ''
        if number % 2 == 0:
            current_answer = 'yes'
        else: 
            current_answer = 'no'
        if answer == current_answer:
            current += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{current_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}')

def main():
    print('Welcome to the Brain Games!')
    welcome_user()



if __name__ == "__main__":
    main()