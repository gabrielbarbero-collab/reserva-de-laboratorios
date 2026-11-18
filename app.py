from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Sala, Reserva
from database import SalaDAO, ReservaDAO

app = Flask(__name__)
CORS(app)

@app.route('/api/salas', methods=['GET'])
def listar_salas():
    dao = SalaDAO()
    return jsonify(dao.listar_todas()), 200

@app.route('/api/salas', methods=['POST'])
def cadastrar_sala():
    dados = request.get_json()
    nova_sala = Sala(
        nome=dados.get('nome'),
        capacidade=dados.get('capacidade'),
        recursos=dados.get('recursos')
    )
    dao = SalaDAO()
    id_gerado = dao.cadastrar(nova_sala)
    return jsonify({"mensagem": "Sala cadastrada com sucesso!", "id_sala": id_gerado}), 201

@app.route('/api/reservas', methods=['GET'])
def listar_reservas():
    dao = ReservaDAO()
    return jsonify(dao.listar_todas()), 200

@app.route('/api/reservas', methods=['POST'])
def cadastrar_reserva():
    dados = request.get_json()
    nova_reserva = Reserva(
        id_utilizador=dados.get('id_utilizador'),
        id_sala=dados.get('id_sala'),
        data=dados.get('data'),
        hora_inicio=dados.get('hora_inicio'),
        hora_fim=dados.get('hora_fim'),
        estado=dados.get('estado', 'Confirmada')
    )
    dao = ReservaDAO()
    id_gerado = dao.cadastrar(nova_reserva)
    return jsonify({"mensagem": "Reserva cadastrada com sucesso!", "id_reserva": id_gerado}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)