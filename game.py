from random import randint

secret = randint(1, 100)
guess = None
guesses = 0
print('Угадайте число от 1 до 100')
while True:
    guesses += 1
    if guesses == 1:
        text = 'Первая попытка'
    elif guesses == 2:
        text = 'Вторая попытка'
    else:
        text = 'Последняя попытка'
    guess = int(input(f'{text} > '))
    if guess == secret:
        print('Вы угадали число!')
        print('''
                                SOME NICE PICTURE
        ''')
        if input('Сыграем еще? "y|n": ') == 'y':
            secret = randint(1, 100)
            guesses = 0
        else:
            print('Спасибо за игру!')
            break
    elif guesses == 3:
        print(f'Вы не угадали. Сектретное число: {secret}')
        break
    else:
        if guess > secret:
            print('Загаданное число меньше. Попробуйте еще раз')
        else:
            print('Загаданное число больше. Попробуйте еще раз')
else:
    print('Вы угадали число! Поздравляем!')
