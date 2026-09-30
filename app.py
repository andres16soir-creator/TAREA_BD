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



conn.execute(
    """
    CREATE TABLE IF NOT EXISTS lectores (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        fecha_registro DATE NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS prestamos (
        id INTEGER PRIMARY KEY,
        fecha TEXT NOT NULL,
        libro_id INTEGER NOT NULL,
        lector_id INTEGER NOT NULL,
        FOREIGN KEY (libro_id) REFERENCES libros (id),
        FOREIGN KEY (lector_id) REFERENCES lectores (id)
    )
    """
)


conn.execute(
    """
    INSERT INTO libros (titulo, autor)
    VALUES ('Cien años de soledad', 'Gabriel Garcia Marquez')
    """
)

conn.execute(
    """
    INSERT INTO lectores (nombre, apellidos, fecha_registro)
    VALUES ('Maria', 'Lopez', '2024-03-10')
    """
)

conn.execute(
    """
    INSERT INTO prestamos (fecha, libro_id, lector_id)
    VALUES ('2024-03-15', 1, 1)
    """
)
conn.commit()