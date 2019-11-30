import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()


email = 't.cruise@gmail.com'
cursor.execute('SELECT * FROM users WHERE email=?', (email,))
print(cursor.fetchone())

email = 'rocklee@gmail.com'
cursor.execute('SELECT * FROM users WHERE email = ? OR name = ?',
               (email, 'Rock Lee'))
print(cursor.fetchone())

cursor.execute('SELECT * FROM users WHERE email = :email OR name = :name',
               {'email': email, 'name': 'Sarah Conor'})
print(cursor.fetchone())

cursor.execute('SELECT * FROM users')
result = cursor.fetchall()
for user in result:
    print(user)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db.row_factory = dict_factory
cursor = db.cursor()

cursor.execute('SELECT * FROM users')
result = cursor.fetchall()
for user in result:
    print(user['name'], user['email'])

cursor.execute('INSERT INTO users (name, email) VALUES ("User 4", "user4@gmail.com")')
cursor.execute('INSERT INTO users (name, email) VALUES ("User 5", "user5@gmail.com")')
db.commit()
print(db.total_changes)

db.close()
