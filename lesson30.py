import os
from random import randint, shuffle
from libs import get_count, get_len

os.chdir(r'c:\Users')
print(os.getcwd())
ld = os.listdir()
print(ld)
shuffle(ld)
print(ld, len(ld))
rnd = randint(0, len(ld)-1)
print(rnd)
print(ld[rnd])

print(get_count('asassin', 's'))
print(get_len('summer'))

gc = get_count # Функции можно присваивать переменным
print(gc('wizard','w'))