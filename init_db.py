import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Maak de tabel als die nog niet bestaat
cursor.execute('''
    CREATE TABLE IF NOT EXISTS item (
        itemId TEXT PRIMARY KEY,
        eventId TEXT NOT NULL,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        imageUrl TEXT
    )
''')

conn.commit()
conn.close()
