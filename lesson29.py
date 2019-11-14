l1 = ["even", 2, "even", 7, "even", 2, "odd", 3]
l2 = ["even", 1, "even", 2, "odd", 4]


def find_odd(arr):
    return arr.index("odd") in arr


print(find_odd(l1))
print(find_odd(l2))


def find_sum(n):
    return sum([i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0])


print(find_sum(5))
print(find_sum(10))

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul", "Susan"]


def names_selector(arr, x):
    return [i for i in arr if len(i) == x]


print(names_selector(names, 5))
