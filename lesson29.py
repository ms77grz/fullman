l1 = ["even", 2, "even", 6, "even", 10, "odd", 3]


def find_odd(arr):
    if arr.index("odd") in arr:
        return True
    else:
        return False


a = find_odd(l1)
print(a)


def find_sum(num):
    x = list(range(1, num + 1))
    return sum([i for i in x if i % 3 == 0 or i % 5 == 0])


print(find_sum(5))
print(find_sum(10))

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul", "Susan"]

def names_selector(arr, x):
    return [i for i in arr if len(i) == x]

print(names_selector(names,5))
