l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Ivanov', 'Petrov', 'Sidorov']

print(l1[4][0])
print(l1[:3])

l1[2] = 'world'
print(l1)

l1[:2] = [10, 15]
print(l1)

l1.extend(['red', 'green', 'blue'])
l1 += ['one', 2, 3.0]
print(l1)

l1.insert(1, 'ONE')
print(l1)

l1.remove('world')
l1.remove('world')
print(l1)

pop_blue = l1.pop(8)
print(pop_blue)

print(l1.index('one'))

print(l1.count(10))

l2 = ['a', 'A', 'i', 'I', 'abc', 'ABC']
l2.sort()
print(l2)

l3 = l2.copy()
print(l3)

l1.clear()
print(l1)
