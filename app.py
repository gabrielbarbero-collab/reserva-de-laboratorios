from flask import Flask, jsonify
from database import ligar_bd

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Servidor Flask do Sistema de Reservas a funcionar perfeitamente!"})

# Nova rota para testar a ligação do Flask à base de dados
@app.route('/teste-bd')
def teste_bd():
    conexao = ligar_bd()
    if conexao:
        conexao.close() # Fechamos a ligação após o teste para libertar recursos
        return jsonify({"status": "sucesso", "mensagem": "O Flask conseguiu comunicar com o MySQL do XAMPP!"})
    else:
        return jsonify({"status": "erro", "mensagem": "Falha na comunicação com a base de dados."}), 500

if __name__ == '__main__':
    app.run(debug=True)