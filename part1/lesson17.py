x = 10
print(x, id(x))
x = 20
print(x, id(x))

s = 'hello'
print(s, id(s))
s += ' world'
print(s, id(s))

y = x
print(x, id(x))
print(y, id(y))

x = 30
print(x, id(x))
print(y, id(y))

l = [1, 2, 3]
print(l, id(l))
l.append(5)
print(l, id(l))

l1 = [1, 2, 3]
l2 = l1
print(l1, id(l1))
print(l2, id(l2))

l1.append(5)
print(l1, id(l1))
print(l2, id(l2))

l3 = l1.copy()
l4 = l1[:]
l1.append(8)
print(l1, id(l1))
print(l2, id(l2))
print(l3, id(l3))
print(l4, id(l4))