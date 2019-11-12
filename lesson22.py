s1 = {'apple', 'pear', 'apple', 'banana', 'orange', 'cherry', 'pear'}
print(s1)
s2 = set('hello')
print(s2)
s3 = {i for i in range(1, 11)}
print(s3)
s4 = set()
print(s4)

nums = [7, 3, 2, 5, 3, 5, 1, 2, 6, 2, 4, 1]
unique = list(set(nums))
print(unique)

a = set('abracadabra')
b = set('alacazam')
c = a - b  # вычитание - убираем из a все буквыб которые есть в b
d = a | b  # объединение - буквы или в a или в b
e = a & b  # пересечение - буквы и в a и в b
f = a ^ b  # множество из уникальных элементов

print(a, b, c, d, e, f, sep='\n')

s5 = s1.copy()
print(s1, id(s1))
print(s5, id(s5))

s5.add('melon')
s5.add('banana')  # повторяющийся элемент добавлен не будет
print(s5)

s5.remove('apple')
print(s5)
try:
    s5.remove('apple')
    print('apple is removed')
except:
    print('no more apples in s5')

# не вызывает ошибки в случае отсутствия удаляемого элемента
s5.discard('apple')
s5.discard('melon')
print(s5)

s5.add('apple')

if 'apple' in s5:
    print('apple is in s5')
else:
    print('no more apples in s5')

poped_item = s5.pop() # удаляет случайный элемент и вызывает ошибку, если множество пустое
print(poped_item, s5)

s5.clear()
print(s5)

fs = frozenset('frozenset')
print(fs)

for i in s1:
    print(i)