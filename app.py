from flask import Flask, jsonify, render_template
from database import ligar_bd

app = Flask(__name__)

# Esta rota agora carrega o ficheiro index.html que criaste na pasta templates
@app.route('/')
def home():
    return render_template('index.html')

# Rota de teste da base de dados que já tínhamos a funcionar
@app.route('/teste-bd')
def teste_bd():
    conexao = ligar_bd()
    if conexao:
        conexao.close()
        return jsonify({"status": "sucesso", "mensagem": "O Flask conseguiu comunicar com o MySQL do XAMPP!"})
    else:
        return jsonify({"status": "erro", "mensagem": "Falha na comunicação com a base de dados."}), 500

if __name__ == '__main__':
    app.run(debug=True)