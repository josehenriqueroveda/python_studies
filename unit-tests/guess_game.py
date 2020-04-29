import random

attempts = 1


def run_guess(guess, answer, attempts):
    if 0 < guess < 11:
        if guess == answer:
            print(f'Congratulations! You got it in {attempts} attempts!')
            return True
    else:
        print('Only numbers 1~10!')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number 1~10: '))
            if run_guess(guess, answer, attempts):
                break
        except ValueError:
            print('Please, enter a number.')
            continue
        attempts += 1