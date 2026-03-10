import random


def prime_number(num):
    if num <= 1:
        return 'no'
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'no'
    return 'yes'
    

START_QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_start():
    number1 = random.randint(1, 100)
    answer = number1
    correct_answer = prime_number(number1)

    return answer, str(correct_answer)