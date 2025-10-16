from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/registro', methods = ("GET", "POST"))
def registro():
    error = None
    if request.method == "POST":
        nombreCompleto = request.form["nombreCompleto"]
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        fechaNAcimiento
    return render_template('registro.html')

@app.route('/iniciosesion')
def iniciosesion():
    return render_template('iniciosesion.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)
