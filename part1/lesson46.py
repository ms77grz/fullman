import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# cursor.execute('INSERT INTO users (name, email) VALUES ("John Smith", "j.smith@gmail.com")')
# cursor.execute('INSERT INTO users (name, email) VALUES ("Sarah Conor", "s.conor@gmail.com")')
# cursor.execute('INSERT INTO users (name, email) VALUES ("Phil Collins", "ph.collins@gmail.com")')
# cursor.execute('INSERT INTO users (name, email) VALUES ("Tom Cruise", "t.cruise@gmail.com")')

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ("Susan Vega", "s.vega@gmail.com");
# INSERT INTO users (name, email) VALUES ("Rick Lee", "r.lee@gmail.com");
# ''')

users = [
    ('User 1', 'user1@gmail.com'),
    ('User 2', 'user2@gmail.com'),
    ('User 3', 'user3@gmail.com'),
]
# cursor.executemany('INSERT INTO users (name, email) VALUES (?,?)', (users))

db.commit()

db.close()
