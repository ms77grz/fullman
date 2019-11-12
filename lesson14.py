l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
l2 = list('hello')
l3 = list((1, 2, 3))
l4 = [i for i in 'hello']
l5 = [i for i in 'hello world' if i != ' ' and i != 'e']
l6 = [i*2 for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]

for i in range(1, 3):
    print(f'Внешний цикл #{i}')
    for j in range(1, 3):
        print(f'\tВнутренний цикл #{j}')

for i in range(1, 10):
    for j in range(2, 10):
        print(f'{i} * {j} = {i*j}\t', end=' ')
    print('')
else:
    print('Well done!')
