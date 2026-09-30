import sqlite3

conn = sqlite3.connect('biblioteca.db')


conn.execute(
    """
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL
    )
    """
)

conn.commit()