# coding=utf-8
def get_sum(a: int, b: int) -> int:
    """Возвращает сумму аргументов a и b."""
    return a + b


print(get_sum(1, 2))

a = 5


def f1():
    """Глобальная переменная a неизменяема. Используется в качестве второго операнда."""
    print(1 + a)


f1()
print(a)


def f2():
    """Создаем локальную переменную a. Изменяем ее и используем в качестве второго операнда.
    Глобальная переменная a никак не изменяется."""
    a = 10
    a += 1
    print(1 + a)


f2()
print(a)


def f3():
    """Глобальная переменная становится доступна для изменений."""
    global a
    a += 34
    print(26 + a)


f3()
print(a)

l = [1, '2', 3]


def f4(l):
    return [i*2 for i in l]


print(f4(l))


def f5(l):
    def get_mult(x):
        return int(x) * 2
    return [get_mult(i) for i in l]


print(f5(l))


def f6(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]

print(f6(l))


def f7(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))

print(f7(l))