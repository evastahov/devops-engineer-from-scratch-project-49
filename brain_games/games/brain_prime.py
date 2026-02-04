import random

MIN_INT = 1
MAX_INT = 50
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_game_data():
    question = random.randint(MIN_INT, MAX_INT)
    answer = 'yes' if is_prime(question) else 'no'
    return [str(question), answer]
