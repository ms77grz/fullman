product1 = {'title': 'Sony', 'price': 100}
print(product1.pop('title'))
print(product1.pop('no_title', 'No such key'))

product2 = {'title': 'iPhone', 'price': 110}
print(product2.popitem())
print(product2.popitem())

product3 = {'title': 'Samsung', 'price': 90}
print(product3.setdefault('title'))
print(product3.setdefault('model', 'A3'))
print(product3)
print(product3.update({'price': 98}))
print(product3)

a, b, c = product3.values()
print(a, b, c)
print(type(a))