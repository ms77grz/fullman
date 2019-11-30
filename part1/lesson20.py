t1 = (1, 2, 3)
t2 = 1, 2, 3  # Упаковка кортежа
a, b, c = t1  # Распаковка кортежа
t3 = tuple((1, 2, 3))
t4 = ()  # Пустой кортеж
t5 = (1,)  # Кортеж с одним единтвенным элементом
t6 = tuple('hello')

l1 = [1, 2, 3]

# Отображение размера объекта в памяти (байты)
print(t1.__sizeof__())
print(l1.__sizeof__())

print('0'*32)
print('0'*24)

t7 = tuple(' world')
t8 = t6 + t7
print(t8, len(t8), t8.count('l'))

if 'a' in t8:
    print(t8.index('a'))
else:
    print('Nothing found')

print(t8.index('d'))

for i in t8:
    if i == ' ':
        continue
    print(f'"{i}"', end=' ')
else:
    print('Done')

t9 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
print(t9, id(t9))

t9[2][0] = 'a'
t9[4].append('English')
print(t9, id(t9))

x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)
