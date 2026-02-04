import random

DESCRIPTION = 'What is the result of the expression?'
MIN_INT = 1
MAX_INT = 10
OPERATORS = ['+', '-', '*']


def get_correct_answer(int_1, operator, int_2):
    match operator:
        case '+':
            return int_1 + int_2
        
        case '-':
            return int_1 - int_2
        
        case '*':
            return int_1 * int_2
        
        case _:
            return None


def generate_game_data():
    int_1 = random.randint(MIN_INT, MAX_INT)
    int_2 = random.randint(MIN_INT, MAX_INT)
    random_operator = random.choice(OPERATORS)
    question = f'{int_1} {random_operator} {int_2}'
    answer = get_correct_answer(int_1, random_operator, int_2)
    return [question, str(answer)]
