 from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Carga el HTML que guardaste

@app.route('/login', methods=['POST'])
def login():
    # Obtén los datos del formulario
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    # Aquí puedes agregar lógica para validar o guardar los datos
    return f"Correo: {correo}, Contraseña: {contraseña}"  # Respuesta temporal

if __name__ == '__main__':
    app.run(debug=True)