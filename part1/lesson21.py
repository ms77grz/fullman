words = ['мадам', 'топот', 'test', 'madam', 'word']
polyndroms = [word for word in words if word[::-1] == word]
print(polyndroms)
for word in words:
    if word[::-1] == word:
        print(word)

my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
for i in my_str:
    if i.lower().replace(' ', '') == i[::-1].lower().replace(' ', ''):
        print(i)

l1 = list(range(1, 10))
print(l1)
l2 = list('hello')
print(l2)
# Приводим списки к строкам с произвольными разделителями
s1 = '-'.join(map(str, l1))
s2 = ','.join(l2)

print(s1)
print(s2)
