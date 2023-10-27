#Função para inserir um aluno no arquivo
def inserir_aluno():
  nome = input("Digite o nome do aluno: ")
  matricula = input("Digite a matrícula do aluno: ")
  curso = input("Digite o curso do aluno: ")

  with open("alunos.txt", "a") as arquivo:
    arquivo.write(f"{nome}, {matricula},{curso}\n")


    #Função para listar os dados dos alunos
def listar_dados():
  with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
      try:
        nome, matricula, curso = linha.strip().split(", ")
        print(f"Nome: {nome}, Matrícula: {matricula}, Curso: {curso}")
      except ValueError:
        print(f"Linha inválida: {linha.strip()}")


#Função para alterar os dados de um aluno
def alterar_aluno():
  matricula_alterar() == input(
      "Digite a matrícula do aluno que deseja alterar: ")
  novos_dados() == input("Digite os novos dados (nome, matrícula, curso): ")

  with open("alunos.txt", "r") as arquivo:
    linhas = arquivo.readlines()

  with open("alunos.txt", "w") as arquivo:
    for linha in linhas:
      if matricula_alterar in linha:
        arquivo.write(novos_dados + "\n")
      else:
        arquivo.write(linha)


#Função para excluir um aluno
def excluir_aluno():
  matricula_excluir = input("Digite a matricula do aluno que deseja excluir: ")

  with open("alunos.txt", "r") as arquivo:
    linhas = arquivo.readlines()
  with open("alunos.txt", "w") as arquivo:
    for linha in linhas:
      if matricula_excluir not in linha:
        arquivo.write(linha)


#Menu Principal
while True:
  print("\nMenu: ")
  print("1. Inserir aluno")
  print("2. listar dados")
  print("3. Alterar dados")
  print("4. Excluir aluno")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    inserir_aluno()
  elif opcao == "2":
    listar_dados()
  elif opcao == "3":
    alterar_aluno()
  elif opcao == "4":
    excluir_aluno()
  elif opcao == "5":
    break
  else:
    print("Opção inválida. Tente novamente.")
