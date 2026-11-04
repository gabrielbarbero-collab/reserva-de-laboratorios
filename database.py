import mysql.connector
from mysql.connector import Error

def ligar_bd():
    try:
        # O XAMPP usa por padrão o utilizador 'root' e palavra-passe em branco
        conexao = mysql.connector.connect(
            host='localhost',
            database='reserva_laboratorios',
            user='root',
            password=''
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida à base de dados MySQL do XAMPP!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

# Testa a conexão executando o ficheiro diretamente
if __name__ == '__main__':
    ligar_bd()