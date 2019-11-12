secret = 35
guess = None
guesses = 0
print('Угадайте число от 1 до 100')
while True:
    guess = int(input('> '))

    guesses += 1
    if guesses == 3:
        print('Вы не угадали')
        break
    elif guess == secret:
        print('Вы угадали число!')
        break
    else:
        print('Попробуйте еще раз')
else:
    print('Вы угадали число! Поздравляем!')

    print('Попробуйте еще раз')
