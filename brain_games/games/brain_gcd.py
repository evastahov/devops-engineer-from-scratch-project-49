import math
import random

MIN_INT = 1
MAX_INT = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game_data():
    int_1 = random.randint(MIN_INT, MAX_INT)
    int_2 = random.randint(MIN_INT, MAX_INT)
    question = f'{int_1} {int_2}'
    answer = math.gcd(int_1, int_2)
    return [question, str(answer)]
