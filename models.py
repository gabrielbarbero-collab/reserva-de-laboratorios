class Utilizador:
    def __init__(self, id_utilizador=None, nome=None, email=None, tipo=None):
        self.id_utilizador = id_utilizador
        self.nome = nome
        self.email = email
        self.tipo = tipo

    def to_dict(self):
        return {
            "id_utilizador": self.id_utilizador,
            "nome": self.nome,
            "email": self.email,
            "tipo": self.tipo
        }

class Sala:
    def __init__(self, id_sala=None, nome=None, capacidade=None, recursos=None):
        self.id_sala = id_sala
        self.nome = nome
        self.capacidade = capacidade
        self.recursos = recursos

    def to_dict(self):
        return {
            "id_sala": self.id_sala,
            "nome": self.nome,
            "capacidade": self.capacidade,
            "recursos": self.recursos
        }

class Reserva:
    def __init__(self, id_reserva=None, id_utilizador=None, id_sala=None, data=None, hora_inicio=None, hora_fim=None, estado="Confirmada"):
        self.id_reserva = id_reserva
        self.id_utilizador = id_utilizador
        self.id_sala = id_sala
        self.data = str(data) if data else None
        self.hora_inicio = str(hora_inicio) if hora_inicio else None
        self.hora_fim = str(hora_fim) if hora_fim else None
        self.estado = estado

    def to_dict(self):
        return {
            "id_reserva": self.id_reserva,
            "id_utilizador": self.id_utilizador,
            "id_sala": self.id_sala,
            "data": self.data,
            "hora_inicio": self.hora_inicio,
            "hora_fim": self.hora_fim,
            "estado": self.estado
        }