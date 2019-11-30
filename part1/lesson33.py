import locale
f = open('file.txt', encoding='utf-8')
print(f.encoding)
text = f.read(3)
print(text)
f.seek(0)
text = f.read(8)
print(text)
f.seek(0)
text = f.read()
print(text)
f.close()

f = open('file.txt', 'a', encoding='utf-8')
f.write('Новая строка\n')
f.close()

lines = ['Новая строка 1', 'Новая строка 2']

f = open('file.txt', 'a', encoding='utf-8')
for line in lines:
    f.write(line + '\n')
f.close()

with open('file.txt', 'a', encoding='utf-8') as f:
    f.writelines(map(lambda line: line + '\n', lines))

with open('file.txt', 'a', encoding='utf-8') as f:
    f.writelines(line + '\n' for line in lines)

with open('file.txt', 'a', encoding='utf-8') as f:
    f.writelines(f'{line}\n' for line in lines)

with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

with open('file.txt', 'w', encoding='utf-8') as f:
    f.writelines(map(lambda line: line + '\n', lines))