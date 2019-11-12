secret = 35
guess = None
guesses = 0
print('Угадайте число от 1 до 100')
while True:
    guess = int(input('> '))
    guesses += 1
    if guess == secret:
        print('Вы угадали число!')
        break
    elif guesses == 3:
        print('Вы не угадали')
        break
    else:
        if guess > secret:
            print('Загаданное число меньше.\nПопробуйте еще раз')
        else:
            print('Загаданное число больше.\nПопробуйте еще раз')
else:
    print('Вы угадали число! Поздравляем!')
