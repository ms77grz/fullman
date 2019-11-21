def hello():
    return 'Hello, I am func "hello"'


def super_func(func):
    print('Hello, I am func "super_func"')
    print(func())


super_func(hello)