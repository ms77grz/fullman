import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE)
''')
db.close()
