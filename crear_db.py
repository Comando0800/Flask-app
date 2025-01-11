import psycopg2
import os

# Configura los detalles de conexión de la base de datos
DATABASE_URL = "postgresql://usuarios_db_845t_user:IXD5YERC6uyfB6GqZjdqU65hR6wvf4Gt@dpg-cu1905btq21c73bgab7g-a/usuarios_db_845t"
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# Crear la tabla 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    correo TEXT NOT NULL,
    contraseña TEXT NOT NULL
)
''')

conn.commit()
print("Base de datos y tabla creadas correctamente.")
conn.close()