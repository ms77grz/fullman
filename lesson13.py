s = 'Hello, world!'
for l in s:
    if l in [' ', ',', '!']:
        continue
    print(f'"{l.lower()}"', end=' ')

print('\nsecond example'.upper())

for i in 'Hello, world!':
    if i == ',':
        break
    print(i, end=' ')
else:
    print('No commas')

print('home work'.upper())

year = 1900

while year <= 2019:
    print(year)
    year += 1
else:
    print('Done')