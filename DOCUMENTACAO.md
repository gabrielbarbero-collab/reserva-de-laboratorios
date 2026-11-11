# Documentação do Projeto - Etapa 1: Modelagem e Base de Dados

**Projeto:** Sistema de Reservas de Laboratórios e Salas de Estudo  
**Autor:** Gabriel Elias / Gabriel Barbero  
**Data de Entrega:** 09/11/2026  

---

## 1. Visão Geral do Sistema
O sistema tem como objetivo gerir as reservas de salas e laboratórios de uma instituição de ensino. Permite listar salas disponíveis, registar utilizadores (alunos e professores) e efetuar reservas em tempo real, garantindo a integridade dos dados através de relações de chaves estrangeiras.

---

## 2. Modelagem Orientada a Objetos (UML - Diagrama de Classes)

### Classes Principais:

1. **Utilizador**
   - `- id_utilizador: int`
   - `- nome: string`
   - `- email: string`
   - `- tipo: string` ('aluno' | 'professor')

2. **Sala**
   - `- id_sala: int`
   - `- nome: string`
   - `- capacidade: int`
   - `- recursos: string`

3. **Reserva**
   - `- id_reserva: int`
   - `- id_utilizador: int` (FK)
   - `- id_sala: int` (FK)
   - `- data: date`
   - `- hora_inicio: time`
   - `- hora_fim: time`
   - `- estado: string`

### Relacionamentos:
- **Utilizador (1) ─── (0..*) Reserva:** Um utilizador pode realizar várias reservas.
- **Sala (1) ─── (0..*) Reserva:** Uma sala pode estar associada a várias reservas em horários distintos.

---

## 3. Modelo Relacional da Base de Dados (MySQL)

### Tabela: `utilizadores`
| Campo | Tipo | Restrições |
| :--- | :--- | :--- |
| `id_utilizador` | INT | PRIMARY KEY, AUTO_INCREMENT |
| `nome` | VARCHAR(100) | NOT NULL |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL |
| `tipo` | ENUM | 'aluno', 'professor', NOT NULL |

### Tabela: `salas`
| Campo | Tipo | Restrições |
| :--- | :--- | :--- |
| `id_sala` | INT | PRIMARY KEY, AUTO_INCREMENT |
| `nome` | VARCHAR(100) | NOT NULL |
| `capacidade` | INT | NOT NULL |
| `recursos` | TEXT | NULLABLE |

### Tabela: `reservas`
| Campo | Tipo | Restrições |
| :--- | :--- | :--- |
| `id_reserva` | INT | PRIMARY KEY, AUTO_INCREMENT |
| `id_utilizador` | INT | FOREIGN KEY (utilizadores) |
| `id_sala` | INT | FOREIGN KEY (salas) |
| `data` | DATE | NOT NULL |
| `hora_inicio` | TIME | NOT NULL |
| `hora_fim` | TIME | NOT NULL |
| `estado` | VARCHAR(20) | DEFAULT 'confirmada' |

---

## 4. Script de Teste e Validação da Conexão
A verificação da comunicação entre a aplicação Python e o MySQL (XAMPP) é realizada através do script `testar_conexao.py`, que executa consultas de contagem simples nas tabelas `salas` e `utilizadores`.
