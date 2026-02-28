from flask import Flask, request

app = Flask(__name__)
# --- R00674692 ---



# --- 1. GET ---
@app.route("/info", methods=["GET"])
def info():
    return {
        "aplicacion": "Sistema Web de Gestión para Clínica Médica",
        "estado": "Activo",
        "descripcion": "API básica para la gestión de la clínica"
    }


# --- 2. POST ---
@app.route("/mensaje", methods=["POST"])
def nuevopaciente():
    data = request.json
    nombre = data.get("nombre del paciente", "Nuevo")
    return {"mensaje": f"Bienvenido, Paciente {nombre}. Tu cuenta se creó con éxito."}, 201




# --- END OF ROUTES ---

if __name__ == "__main__":
    app.run(debug=True)