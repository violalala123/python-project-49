import random

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
  
    print('Answer "yes" if the number is even, otherwise answer "no".')
    current = 0
    while current < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        cur = ''
        if number % 2 == 0:
            cur = 'yes'
        else: 
            cur = 'no'
        if answer == cur:
            current += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cur}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == "__main__":
    main()