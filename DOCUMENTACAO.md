# Documentação da Etapa 1 - Sistema de Reservas de Laboratório

## 1. Introdução
Este documento apresenta a especificação de requisitos, a modelagem UML e a estrutura do banco de dados relacional para o Sistema de Reservas de Laboratório, desenvolvido com Flask, MySQL e HTML/CSS/JS.

---

## 2. Levantamento de Requisitos

### 2.1 Requisitos Funcionais (RF)
- **RF01 - Gestão de Utilizadores:** O sistema deve permitir o registo, autenticação e gestão de utilizadores (Alunos, Professores e Administradores).
- **RF02 - Gestão de Salas/Laboratórios:** O sistema deve permitir visualizar a lista de laboratórios disponíveis, as suas capacidades e os seus recursos.
- **RF03 - Realização de Reservas:** O sistema deve permitir que um utilizador selecione um laboratório, data e horário para realizar uma reserva.
- **RF04 - Validação de Conflitos:** O sistema deve impedir que duas reservas sejam efetuadas para o mesmo laboratório no mesmo dia e intervalo de horário.
- **RF05 - Cancelamento e Alteração:** O sistema deve permitir que o utilizador cancele ou altere as suas próprias reservas.

### 2.2 Requisitos Não Funcionais (RNF)
- **RNF01 - Desempenho:** A consulta de disponibilidade de salas deve responder em menos de 2 segundos.
- **RNF02 - Usabilidade:** A interface web deve ser intuitiva e responsiva para computadores e dispositivos móveis.
- **RNF03 - Segurança:** As palavras-passe dos utilizadores devem ser armazenadas com encriptação no banco de dados.
- **RNF04 - Disponibilidade:** O banco de dados MySQL deve estar configurado no ambiente local XAMPP para execução dos testes.

---

## 3. Diagramas UML

### 3.1 Diagrama de Casos de Uso
![Diagrama de Casos de Uso](img/casos_de_uso.png)

*Descrição dos Casos de Uso:*
- **UC01 - Registar/Login:** Permite acesso autenticado ao sistema.
- **UC02 - Consultar Laboratórios:** Exibe as salas e recursos.
- **UC03 - Reservar Laboratório:** Cria o agendamento de um horário.
- **UC04 - Gerir Reservas:** Permite visualizar e cancelar agendamentos.

---

### 3.2 Diagrama de Classes
![Diagrama de Classes](img/diagrama.png)

```mermaid
classDiagram
    class Utilizador {
        +int id_utilizador
        +string nome
        +string email
        +string tipo
    }

    class Sala {
        +int id_sala
        +string nome
        +int capacidade
        +string recursos
    }

    class Reserva {
        +int id_reserva
        +int id_utilizador
        +int id_sala
        +date data
        +time hora_inicio
        +time hora_fim
        +string estado
    }

    Utilizador "1" -- "0..*" Reserva : realiza
    Sala "1" -- "0..*" Reserva : contem