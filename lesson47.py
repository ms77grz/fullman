import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()


email = 't.cruise@gmail.com'
cursor.execute('SELECT * FROM users WHERE email=?', (email,))
result = cursor.fetchone()
print(result)

db.close()