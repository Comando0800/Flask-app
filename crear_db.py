import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    correo TEXT NOT NULL,
    contraseña TEXT NOT NULL
)
''')

conn.close()
print("Base de datos creada correctamente.")