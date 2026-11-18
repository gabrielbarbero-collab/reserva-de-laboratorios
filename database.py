import mysql.connector
from models import Sala, Reserva

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="reserva_laboratorios"
    )

class SalaDAO:
    def listar_todas(self):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM salas")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Sala(r['id_sala'], r['nome'], r['capacidade'], r['recursos']).to_dict() for r in resultados]

    def cadastrar(self, sala: Sala):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO salas (nome, capacidade, recursos) VALUES (%s, %s, %s)"
        cursor.execute(sql, (sala.nome, sala.capacidade, sala.recursos))
        conexao.commit()
        id_gerado = cursor.lastrowid
        cursor.close()
        conexao.close()
        return id_gerado

class ReservaDAO:
    def listar_todas(self):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reservas")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Reserva(r['id_reserva'], r['id_utilizador'], r['id_sala'], r['data'], r['hora_inicio'], r['hora_fim'], r['estado']).to_dict() for r in resultados]

    def cadastrar(self, reserva: Reserva):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO reservas (id_utilizador, id_sala, data, hora_inicio, hora_fim, estado) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (reserva.id_utilizador, reserva.id_sala, reserva.data, reserva.hora_inicio, reserva.hora_fim, reserva.estado))
        conexao.commit()
        id_gerado = cursor.lastrowid
        cursor.close()
        conexao.close()
        return id_gerado