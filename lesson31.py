from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, '')

# date
today = date.today()
print(today)  # 2019-11-15
print(today.day)  # 15
print(today.month)  # 11
print(today.year)  # 2019
print(today.weekday())  # 4
print(today.isoweekday())  # 5

# datetime
now = datetime.now()
print(now)
now = datetime.today()
print(now)

print(now.day)  # 15
print(now.month)  # 11
print(now.year)  # 2019
print(now.weekday())  # 4
print(now.isoweekday())  # 5
print(now.hour)  # 15
print(now.minute)  # 41
print(now.second)  # 52
print(now.microsecond)  # 987163

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()])

print(now.strftime('%A'))
