import random


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


start_quest = 'Find the greatest common divisor of given numbers.'


def game_start():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    answer = f'{number1} {number2}'
    correct_answer = str(get_gcd(number1, number2))
#    while number2:
#       number1, number2 = number2, number2 % number2
#       correct_answer = number1
    return answer, str(correct_answer)

    
    
        
