import tkinter as tk
import sqlite3

# Cria a conexão com o banco de dados
conn = sqlite3.connect('alunos.db')

# Exclui a tabela de alunos, se já existir
conn.execute("DROP TABLE IF EXISTS ALUNOS")

# Cria a tabela de alunos com a nova coluna
conn.execute('''CREATE TABLE ALUNOS
  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    MATRICULA TEXT NOT NULL,
    CURSO TEXT NOT NULL);''')


# Função para adicionar um novo aluno
def adicionar_aluno(nome, matricula, curso):
  conn.execute(
      "INSERT INTO ALUNOS (NOME, MATRICULA, CURSO) \
                VALUES (?, ?, ?)", (nome, matricula, curso))
  conn.commit()
  print("Aluno adicionado com sucesso!")


# Função para atualizar dados de um aluno
def atualizar_aluno(id, nome, matricula, curso):
  conn.execute(
      "UPDATE ALUNOS SET NOME = ?, MATRICULA = ?, CURSO = ? \
            WHERE ID = ?", (nome, matricula, curso, id))
  conn.commit()
  print("Dados do aluno atualizados com sucesso!")


# Função para excluir um aluno pelo ID
def excluir_aluno(id):
  conn.execute("DELETE FROM ALUNOS WHERE ID = ?", (id, ))
  conn.commit()
  print("Aluno excluído com sucesso!")


# Função para buscar todos os alunos cadastrados
def listar_alunos():
  cursor = conn.execute("SELECT ID, NOME, MATRICULA, CURSO from ALUNOS")
  for row in cursor:
    print("ID = ", row[0])
    print("NOME = ", row[1])
    print("MATRÍCULA = ", row[2])
    print("CURSO = ", row[3], "\n")


# Função para buscar um aluno pelo ID
def buscar_aluno(id):
  cursor = conn.execute(
      "SELECT ID, NOME, MATRICULA, CURSO from ALUNOS \
            WHERE ID = ?", (id, ))
  row = cursor.fetchone()
  if row is not None:
    print("ID = ", row[0])
    print("NOME = ", row[1])
    print("MATRÍCULA = ", row[2])
    print("CURSO = ", row[3])
  else:
    print("Aluno não encontrado.")


# Menu principal
while True:
  print("\n------ Gerenciamento de Alunos ------")
  print("1. Adicionar aluno")
  print("2. Atualizar dados do aluno")
  print("3. Excluir aluno")
  print("4. Listar todos os alunos")
  print("5. Buscar aluno por ID")
  print("6. Sair")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula do aluno: ")
    curso = input("Curso do aluno: ")
    adicionar_aluno(nome, matricula, curso)
  elif opcao == "2":
    id = input("ID do aluno a ser atualizado: ")
    nome = input("Novo nome do aluno: ")
    matricula = input("Nova matrícula do aluno: ")
    curso = input("Novo curso do aluno: ")
    atualizar_aluno(id, nome, matricula, curso)
  elif opcao == "3":
    id = input("ID do aluno a ser excluído: ")
    excluir_aluno(id)
  elif opcao == "4":
    listar_alunos()
  elif opcao == "5":
    id = input("ID do aluno a ser buscado: ")
    buscar_aluno(id)
  elif opcao == "6":
    print("programa fechado")
    conn.close()
    break
  else:
    print("Opção inválida.")
