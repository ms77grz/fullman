def hello():
    return 'Hello, I am func "hello"'


def super_func(func):
    print('Hello, I am func "super_func"')
    print(func())


super_func(hello)
test = hello
print(test())


def my_decorator(func):
    def func_wrapper():
        print('Code before')
        func()
        print('Code after')
    return func_wrapper


@my_decorator
def func_test():
    print('Hello, I am func "func_test"')


# test = my_decorator(func_test)
# test()
func_test()


def make_title(func):
    def wrapper():
        title = func()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapper


@make_title
def hello_world():
    return 'hello, world'


print(hello_world())
