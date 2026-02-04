import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_INT = 1
MAX_INT = 50


def generate_game_data():
    question = random.randint(MIN_INT, MAX_INT)
    answer = 'yes' if question % 2 == 0 else 'no'
    return [str(question), answer]
