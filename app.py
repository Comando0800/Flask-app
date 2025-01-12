from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Ruta principal para cargar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    # Verificar que los campos no estén vacíos
    if not correo or not contraseña:
        return "Por favor ingrese ambos, correo y contraseña"

    # Generar un hash de la contraseña
    hashed_password = generate_password_hash(contraseña)

    # Conectar a la base de datos y guardar los datos
    try:
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (correo, contraseña) VALUES (?, ?)", (correo, hashed_password))
        conn.commit()
    except sqlite3.Error as e:
        app.logger.error(f"Error al insertar datos: {e}")
        return "Hubo un error al guardar los datos"
    finally:
        conn.close()

    return "Datos guardados exitosamente"

if __name__ == '__main__':
    app.run(debug=True)
