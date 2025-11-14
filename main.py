from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Ejercicio 1: Compra de tarros de pintura
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = error = None
    valores = {"nombre": "", "edad": "", "tarros": ""}

    if request.method == "POST":
        try:
            # Tomar valores y guardarlos para persistir en la vista
            valores["nombre"] = request.form.get("nombre", "").strip()
            valores["edad"] = request.form.get("edad", "").strip()
            valores["tarros"] = request.form.get("tarros", "").strip()

            # Validar que no vengan vacíos
            if valores["nombre"] == "" or valores["edad"] == "" or valores["tarros"] == "":
                error = "Por favor, completa todos los campos."
            else:
                edad = int(valores["edad"])
                tarros = int(valores["tarros"])

                if edad < 0 or tarros <= 0:
                    error = "La edad debe ser mayor o igual a 0 y la cantidad de tarros debe ser mayor a 0."
                else:
                    precio_tarro = 9000
                    total_sin_desc = precio_tarro * tarros

                    # Cálculo del descuento según la edad
                    if edad < 18:
                        porcentaje_desc = 0
                    elif 18 <= edad <= 30:
                        porcentaje_desc = 0.15
                    else:  # mayores a 30
                        porcentaje_desc = 0.25

                    monto_descuento = total_sin_desc * porcentaje_desc
                    total_con_desc = total_sin_desc - monto_descuento

                    resultado = {
                        "nombre": valores["nombre"],
                        "total_sin_desc": total_sin_desc,
                        "porcentaje_desc": int(porcentaje_desc * 100),
                        "total_con_desc": total_con_desc
                    }

        except ValueError:
            error = "Por favor, ingresa solo números válidos en edad y cantidad de tarros."

    return render_template("ejercicio1.html", resultado=resultado, error=error, valores=valores)

# Ejercicio 2: Login de usuarios
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = error = None
    valores = {"usuario": "", "clave": ""}

    if request.method == "POST":
        valores["usuario"] = request.form.get("usuario", "").strip()
        valores["clave"] = request.form.get("clave", "").strip()

        usuarios = {
            "juan": "admin",
            "pepe": "user"
        }

        if valores["usuario"] in usuarios and valores["clave"] == usuarios[valores["usuario"]]:
            if valores["usuario"] == "juan":
                resultado = "Bienvenido administrador juan"
            else:  # pepe
                resultado = "Bienvenido usuario pepe"
        else:
            error = "Usuario o contraseña incorrecta"

    return render_template("ejercicio2.html", resultado=resultado, error=error, valores=valores)

# Página extra (Acerca del proyecto)
@app.route("/acerca")
def acerca():
    return render_template("acerca.html")


if __name__ == "__main__":
    app.run(debug=True)
