import random

MIN_INT = 1
MAX_INT = 50
PROGRESSION_LENGTH = 10
FIRST_INT = random.randint(MIN_INT, MAX_INT)
STEP_COUNT = random.randint(MIN_INT, MAX_INT)
DESCRIPTION = 'What number is missing in the progression?'


def create_progression(first, step, max_length):
    return [first + i * step for i in range(max_length)]


def create_mask(coll, index, mask='..'):
    str_coll = [str(i) for i in coll]
    str_coll[index] = mask
    return str_coll


def generate_game_data():
    random_index = random.randint(0, PROGRESSION_LENGTH - 1)
    progression = create_progression(FIRST_INT, STEP_COUNT, PROGRESSION_LENGTH)
    question = ' '.join(create_mask(progression, random_index))
    answer = str(progression[random_index])
    return [question, answer]
