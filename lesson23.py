d = {}
product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title='iPhone', price=110)

print(product1)
print(product2)

l_users = [
    ['john@gmail.com', 'John'],
    ['susan@gamil.com', 'Susan'],
    ['bob@gmail.com', 'Bob']
]
t_users = (
    ('john@gmail.com', 'John'),
    ('susan@gamil.com', 'Susan'),
    ('bob@gmail.com', 'Bob')
)

print(l_users)
print(t_users)

dlu = dict(l_users)
dtu = dict(t_users)
print(dlu)
print(dtu)

product3 = dict.fromkeys(['price1', 'price2', 'price3'], 0.0)
print(product3)

nums = {i: i*i for i in range(1, 11)}
print(nums)
print(nums[1])

print(product1['title'])
print(product1.get('not_title', 'No data'))
print(product1.get('title', 'No data'))

for key in product1:
    print(f'{key}: {product1[key]}')

print(product1.items())
for k, v in product1.items():
    print(f'{k}: {v}')

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]

for i in products:
    for k, v in i.items():
        print(f'{k}: {v}')

for product in products:
    print(product['title'], product['price'])

a, b = product1.items()
print(a[1], b[1])
