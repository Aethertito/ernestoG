from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

# Usuario registrado
usuarios_registrados = {
    "lauro": hashlib.sha256("soto".encode()).hexdigest()
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

        if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena_hash:
            return redirect(url_for("bienvenida"))
        else:
            return "❌ Usuario o contraseña incorrectos"

    return render_template("login.html")

@app.route("/bienvenida")
def bienvenida():
    return render_template("bienvenida.html")

if __name__ == "__main__":
    app.run(debug=True)
