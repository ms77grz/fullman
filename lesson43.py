# lambda - функции


def get_square(num):
    return num ** 2


print(get_square(5))

print((lambda num: num ** 2)(10))

l = [1, 2, 3]
print(list(map(lambda i: i * 2, l)))
