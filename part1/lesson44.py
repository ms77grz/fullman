# регулярные выражения
import re

s = 'Это просто строка текста. А это еще одна строка текста.'
pattern = 'строка'
print(s.find(pattern))
print(pattern in s)

if re.search(pattern, s):
    print('resulted')
else:
    print('not resulted')

result = re.search(pattern, s)

print(result)
print(result.group())
print(result.span())
print(result.start())
print(result.end())

result = re.match(pattern, s)
print(result)
pattern = 'Это'
result = re.match(pattern, s)
print(result)
print(result.group())

pattern = 'строка'
result = re.findall(pattern, s)
print(result)

result = re.split('.', s)
print(result)
print(len(result))
print(len(s))

result = re.split(r'\.', s, maxsplit=1)
print(result)

s = '''Это просто строка текста.
А это еще одна строка текста.
А это строка с цифрами: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
А это строка с разными символами: "!", "@", "-", "&", "?","_"
a\\b\tc
test string'''

pattern = r'\w'
result = re.findall(pattern, s)
print(result)

pattern = r'\w+'
result = re.findall(pattern, s)
print(result)

pattern = r'[эт]'
result = re.findall(pattern, s)
print(result)
print(result.count('т'))
print(result.count('э'))

pattern = r'[эт]+'
result = re.findall(pattern, s)
print(result)

pattern = r'[а-я]+'
result = re.findall(pattern, s)
print(result)

pattern = r'[а-яА-Я0-9]+'
result = re.findall(pattern, s)
print(result)

pattern = r'[а-я]+'
result = re.findall(pattern, s, re.IGNORECASE)
print(result)

pattern = r'[0-3]+'
result = re.findall(pattern, s)
print(result)

pattern = r'\d'
result = re.findall(pattern, s)
print(result)

pattern = r'\d+'
result = re.findall(pattern, s)
print(result)

pattern = r'[\da-]+'
result = re.findall(pattern, s)
print(result)

pattern = r'a\\b\tc'
result = re.findall(pattern, s)
print(result)

pattern = r'^\w+'
result = re.findall(pattern, s)
print(result)

pattern = r'\w+$'
result = re.findall(pattern, s)
print(result)

emails = 'john@gmail.com', 'smith@bank', 'kate@ukraine.com.ua'


def validate_email(email):
    try:
        return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE).group()
    except:
        return "It's not email"


for email in emails:
    print(validate_email(email))
