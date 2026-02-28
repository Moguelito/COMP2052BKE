# NUEVO / MODULE 2 LESSON 3 / NUEVO

from flask import Flask, jsonify, request

app = Flask(__name__)

# {}, memory storage to simulate a database
clinic_staff = {}

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "aplicacion": "Sistema Web de Gestión para Clínica Médica",
        "estado": "Activo",
        "descripcion": "API básica para la gestión de la clínica"
    })

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    
    # validation, email & name
    if not data or "nombre" not in data or "correo" not in data:
        return jsonify({"message": "ERROR: Missing name or email"}), 400

    # id creation
    new_id = len(clinic_staff) + 1
    

    new_user = {
        "id": new_id,
        "nombre": data["nombre"],
        "correo": data["correo"],
        "roles": ["staff"] 
    }
    
    # store in database
    clinic_staff[new_id] = new_user
    
    return jsonify({"usuario": new_user}), 201

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    # dictionary shown as list
    return jsonify(list(clinic_staff.values()))

if __name__ == '__main__':
    app.run(debug=True)