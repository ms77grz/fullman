l1 = [1, 2, 3]
l2 = [i*2 for i in l1]
print(l2)

total = sum([i**2 for i in l1])
print(total)

time = [3, 6.7, 11.8]
for i in time:
    print(int(i*0.5))

s = 'Hello world'
if ' ' in s:
    print(s.upper())
else:
    print(s.lower())
