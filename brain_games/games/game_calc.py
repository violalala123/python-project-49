import random
start_quest = 'What is the result of the expression?'
def game_calc():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    sign = ['+', '-', '*']
    result  = random.choice(sign)
    answer = f'{number1} {result} {number2}'
    match result:
        case '+':
            correct_answer = number1 + number2
        case '-':
            correct_answer = number1 - number2
        case '*':
            correct_answer = number1 * number2
    return answer, str(correct_answer)

    
    
        
