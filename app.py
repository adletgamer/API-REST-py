from flask import Flask, jsonify, request 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

infectados = [
    {"id": 1, "nombre": "Runner", "nivel_peligro": "Bajo", "zona": "Pittsburgh", "es_mutacion": False},
    {"id": 2, "nombre": "Cliker", "nivel_peligro": "Alto", "zona": "Boston", "es_mutacion": True}
]

# Método GET /infectados/<id>
@app.route('/infectados/<int:id>', methods=['GET'])
def get_infectados():
        return jsonify(infectados)

# POST /infectados
@app.route('/infectados', methods=['POST'])
def add_infectados():
    nuevo = request.json
    nuevo["id"] = len(infectados) + 1
    infectados.append(nuevo)
    return jsonify(nuevo), 201

# PUT /infectados/<id>
@app.route('/infectados/<int:id>', methods=['PUT'])
def actualiza_infectado(id):
    for i in infectados:
        if i["id"] == id:
            i.update(request.json)
            return jsonify(i)
    return {"error": "Infectado no encontrado"}, 404

# DELETE /infectados/<id>
@app.route('/infectados/<int:id>', methods=['DELETE'])
def eliminar_infectados(id):
    global infectados
    infectados = [i for i in infectados if i["id"] != id]
    return {"mensaje": "Infectado eliminado"}, 200
