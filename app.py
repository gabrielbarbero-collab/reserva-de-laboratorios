from flask import Flask, jsonify

app = Flask(__name__)

# Rota de teste para garantir que o Flask está a funcionar
@app.route('/')
def home():
    return jsonify({"mensagem": "Servidor Flask do Sistema de Reservas a funcionar perfeitamente!"})

if __name__ == '__main__':
    # O debug=True faz com que o servidor reinicie automaticamente se alterares o código
    app.run(debug=True)