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
        return jsonify({"erro": "Erro ao ligar à base de dados"}), 500
    
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM salas ORDER BY nome ASC")
        salas = cursor.fetchall()
        return jsonify(salas), 200
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500
    finally:
        cursor.close()
        conexao.close()

@app.route('/api/utilizadores', methods=['GET'])
def listar_utilizadores():
    conexao = ligar_bd()
    if not conexao:
        return jsonify({"erro": "Erro ao ligar à base de dados"}), 500
    
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id_utilizador, nome FROM utilizadores ORDER BY nome ASC")
        utilizadores = cursor.fetchall()
        return jsonify(utilizadores), 200
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500
    finally:
        cursor.close()
        conexao.close()

@app.route('/api/reservas', methods=['GET', 'POST'])
def gerir_reservas():
    conexao = ligar_bd()
    if not conexao:
        return jsonify({"mensagem": "Erro ao ligar à base de dados"}), 500

    # OBTER LISTA DE RESERVAS (GET)
    if request.method == 'GET':
        try:
            cursor = conexao.cursor(dictionary=True)
            query = """
                SELECT r.id_reserva, 
                       DATE_FORMAT(r.data, '%d/%m/%Y') AS data,
                       TIME_FORMAT(r.hora_inicio, '%H:%i') AS hora_inicio,
                       TIME_FORMAT(r.hora_fim, '%H:%i') AS hora_fim,
                       r.estado,
                       u.nome AS nome_utilizador, 
                       s.nome AS nome_sala
                FROM reservas r
                JOIN utilizadores u ON r.id_utilizador = u.id_utilizador
                JOIN salas s ON r.id_sala = s.id_sala
                ORDER BY r.id_reserva DESC
            """
            cursor.execute(query)
            reservas = cursor.fetchall()
            return jsonify(reservas), 200
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500
        finally:
            cursor.close()
            conexao.close()

    # CRIAR NOVA RESERVA (POST)
    if request.method == 'POST':
        dados = request.get_json()
        
        campos_obrigatorios = ['id_utilizador', 'id_sala', 'data', 'hora_inicio', 'hora_fim']
        if not dados or not all(k in dados and dados[k] for k in campos_obrigatorios):
            conexao.close()
            return jsonify({"mensagem": "Todos os campos são obrigatórios."}), 400

        if dados['hora_inicio'] >= dados['hora_fim']:
            conexao.close()
            return jsonify({"mensagem": "A hora de fim deve ser superior à hora de início."}), 400

        try:
            cursor = conexao.cursor(dictionary=True)

            # Validação de Conflito de Horários
            query_conflito = """
                SELECT id_reserva FROM reservas 
                WHERE id_sala = %s 
                  AND data = %s 
                  AND (hora_inicio < %s AND hora_fim > %s)
            """
            cursor.execute(query_conflito, (
                dados['id_sala'], 
                dados['data'], 
                dados['hora_fim'], 
                dados['hora_inicio']
            ))
            if cursor.fetchone():
                return jsonify({"mensagem": "A sala já se encontra reservada para este horário."}), 409

            # Inserção da reserva
            query_inserir = """
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
            cursor.execute(query_inserir, valores)
            conexao.commit()

            return jsonify({"mensagem": "Reserva efetuada e confirmada com sucesso!"}), 201

        except Exception as e:
            conexao.rollback()
            return jsonify({"mensagem": f"Falha na transação: {str(e)}"}), 500

        finally:
            cursor.close()
            conexao.close()

if __name__ == '__main__':
    app.run(debug=True)