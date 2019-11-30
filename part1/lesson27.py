def capsy(words):
    if ' ' in words:
        return words.upper()
    else:
        return words.lower()


print(capsy('Hello world'))
print(capsy('Congratulations!'))


def get_sum(a, b, c=0, d=1):
    return a + b + c + d
    '''
    a, b - позиционные аргументы
    c, d - именованные аргументы + аргументы по умолчанию
    '''


print(get_sum(1, 2, 5, 7))
print(get_sum(1, 2, d=15))
print(get_sum(1, 2))
# именованные аргументы всегда после позиционных, но могут быть в любой последовательности
print(get_sum(1, 2, d=10, c=15))


def my_func(*args, **kwargs):
    # *args - позиционные аргументы преобразуются в кортеж
    # **kwargs - именованные аргументы преобразуются в словарь
    pass


def my_func_args_print(*args):
    print(args)


my_func_args_print(1, 2, 3)


def my_func_args_sum(*args):
    return sum(args)


print(my_func_args_sum(10, 20, 30, 40))


def my_func_kwargs(**kwargs):
    print(kwargs)


my_func_kwargs(a=1, b=2, c=3)

# *args, **kwargs - опциональные аргументы
def my_func_advanced(a, b, *args, **kwargs):
    print(a)
    print(b)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


my_func_advanced('a', 'b', 'one', 'two', name='Max', age=42)
my_func_advanced(1,2)