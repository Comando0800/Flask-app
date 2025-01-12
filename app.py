from flask import Flask, render_template, request
import sqlite3

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

    # Conectar a la base de datos y guardar los datos
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (correo, contraseña) VALUES (?, ?)", (correo, contraseña))
    conn.commit()
    conn.close()

    return "Datos guardados exitosamente"

if __name__ == '__main__':
    app.run(debug=True)