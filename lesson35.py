def divide(a,b):
    try:
        return a / b
    except Exception as e:
        print(e)
        return 0.0

print(divide(10,0))

while True:
    try:
        num = int(input('Enter a number: '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('The number must be > 0')
    except ValueError:
        print('Must be a number')
