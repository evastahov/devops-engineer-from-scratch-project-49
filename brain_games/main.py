from brain_games.cli import welcome_user

ROUND_COUNT = 3


def run_game(game):
    user_name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(ROUND_COUNT):
        question, answer = game.generate_game_data()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.\n"
                f"Let's try again, {user_name}"
            )
            return
    print(f'Congratulations, {user_name}!')
