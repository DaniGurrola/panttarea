from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  

usuarios = {}

@app.route('/')
def inicio():
    
    if 'usuario' in session:
        return render_template('index.html', sesion_iniciada=True)
    return render_template('index.html', sesion_iniciada=False)

@app.route('/animales')
def animales():
    if 'usuario' not in session:  
        return redirect(url_for('inicio'))  
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    if 'usuario' not in session:
        return redirect(url_for('inicio'))
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    if 'usuario' not in session:
        return redirect(url_for('inicio'))
    return render_template('maravillas.html')

@app.route('/registro', methods=["GET", "POST"])
def registro():
    if 'usuario' in session:
        return redirect(url_for('inicio'))  

    if request.method == "POST":
        nombreCompleto = request.form["nombreCompleto"]
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        
        
        if password != confirmPassword:
            return render_template('registro.html', error="Las contraseñas no coinciden")
        
        
        if email in usuarios:
            return render_template('registro.html', error="El correo electrónico ya está registrado")
        
        
        hashed_password = generate_password_hash(password)
        
        
        usuarios[email] = {'nombreCompleto': nombreCompleto, 'password': hashed_password}
        
        return redirect(url_for('iniciosesion'))
    
    return render_template('registro.html')

@app.route('/iniciosesion', methods=["GET", "POST"])
def iniciosesion():
    if 'usuario' in session:
        return redirect(url_for('inicio')) 

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        
        if email not in usuarios:
            return render_template('iniciosesion.html', error="Correo o contraseña incorrectos")
        
        
        user = usuarios[email]
        if not check_password_hash(user['password'], password):
            return render_template('iniciosesion.html', error="Correo o contraseña incorrectos")
        
        
        session['usuario'] = email
        return redirect(url_for('inicio'))
    
    return render_template('iniciosesion.html')

@app.route('/cerrarsesion')
def cerrarsesion():
    session.pop('usuario', None)  # Eliminamos el usuario de la sesión
    return redirect(url_for('inicio'))

@app.route('/acerca')
def acerca():
    if 'usuario' not in session:
        return redirect(url_for('inicio'))
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)
