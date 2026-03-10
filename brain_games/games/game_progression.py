import random


def prog(start, step, index):
    progression = []
    for i in range(index):
        progression.append(str(start + i * step))
    return progression


START_QUEST = 'What number is missing in the progression?'


def game_start():
    start = random.randint(1, 30)
    step = random.randint(1, 10)
    index = random.randint(5, 10)
    random_index = random.randint(0, index - 1)
    progression = prog(start, step, index)
    correct_answer = progression[random_index]
    seee = progression.copy()
    seee[random_index] = '..'
    answer = ' '.join(seee)

    return answer, str(correct_answer)









