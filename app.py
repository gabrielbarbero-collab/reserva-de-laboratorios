from flask import Flask, jsonify, render_template, request
from database import ligar_bd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/salas', methods=['GET'])
def listar_salas():
    conexao = ligar_bd()
    if not conexao:
        return jsonify({"erro": "Erro de ligação à base de dados"}), 500
    
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM salas")
    salas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(salas)

@app.route('/api/utilizadores', methods=['GET'])
def listar_utilizadores():
    conexao = ligar_bd()
    if not conexao:
        return jsonify({"erro": "Erro de ligação à base de dados"}), 500
    
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT id_utilizador, nome FROM utilizadores")
    utilizadores = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(utilizadores)

@app.route('/api/reservas', methods=['POST'])
def criar_reserva():
    dados = request.get_json()
    conexao = ligar_bd()
    if not conexao:
        return jsonify({"mensagem": "Erro de ligação à base de dados"}), 500

    try:
        cursor = conexao.cursor()
        query = """
            INSERT INTO reservas (id_utilizador, id_sala, data, hora_inicio, hora_fim, estado)
            VALUES (%s, %s, %s, %s, %s, 'confirmada')
        """
        valores = (
            dados['id_utilizador'],
            dados['id_sala'],
            dados['data'],
            dados['hora_inicio'],
            dados['hora_fim']
        )
        cursor.execute(query, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        return jsonify({"mensagem": "Reserva efetuada com sucesso!"}), 201
    except Exception as e:
        return jsonify({"mensagem": f"Erro ao criar reserva: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)