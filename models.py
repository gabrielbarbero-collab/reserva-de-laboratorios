class Utilizador:
    def __init__(self, id_utilizador, nome, email, tipo):
        self.id_utilizador = id_utilizador
        self.nome = nome
        self.email = email
        self.tipo = tipo  # 'aluno' ou 'professor'

class Sala:
    def __init__(self, id_sala, nome, capacidade, recursos):
        self.id_sala = id_sala
        self.nome = nome
        self.capacidade = capacidade
        self.recursos = recursos

class Reserva:
    def __init__(self, id_reserva, id_utilizador, id_sala, data, hora_inicio, hora_fim, estado='confirmada'):
        self.id_reserva = id_reserva
        self.id_utilizador = id_utilizador
        self.id_sala = id_sala
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.estado = estado