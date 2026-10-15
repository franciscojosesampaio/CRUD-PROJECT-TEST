#Criando um CRUD experimental
#importando as bibliotecas necessárias
import os
import time
import sqlite3

#Função Para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Inicializando a conexão com o banco de dados    
conexao = sqlite3.Connection("sistem_jogos.db")
#o cursor é necessário para poder acessar o banco de dados 
cursor = conexao.cursor()
#o 'execute()' é o que será feito, por exemplo abaixo está sendo criado uma tabela caso elá não exista
cursor.execute("""
               CREATE TABLE IF NOT EXISTS jogos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    preco DECIMAL(4,2) NOT NULL
                    )
               """
               )

#Função Create
def cadastrar(nome, genero, preco):
    #O cursor abaixo está sendo utilizado para realizar inserção de dados na tabela jogos
    cursor.execute(
        "INSERT INTO jogos (nome, genero, preco) VALUES (?, ?, ?)",(nome, genero, preco)
        )
    #o 'commit()' é utilizado para confirma a trasação de dados entre aplicação e banco de dados
    conexao.commit()
    print(f"Jogo {nome} cadastrado com sucesso")

#Função Read
def listar_jogos():
    #o cursor abaixo está realizando um "SELECT" na tabela preço, assim trazendo informações guardadas no db
    cursor.execute("SELECT id, nome, genero, preco FROM jogos")
    #o 'fetchall()' é utilizado para recuperar todas as linhas restantes de um conjunto de resultados após a execução
    #de uma consulta em um db
    jogos = cursor.fetchall()
    #o if abaixo está verificando se a lista de jogos está vazia, caso esteja, será exibido uma mensagem informando que não há jogos cadastrados no sistema
    if not jogos:
        print("\nNenhum jogo cadastrado no sistema! :(")
        return
    
    print("\n --- Lista de Jogos ---")
    #O laço de repetição abaixo está percorrendo a lista de jogos e exibindo as informações de cada jogo já cadastrado no sistema
    for jogo in jogos:
        id_jogo, nome, genero, preco = jogo
        print(f"ID: {id_jogo} | " 
              f"NOME: {nome} | "
              f"GENERO: {genero} | "
              f"PRECO : {preco:.2f}")
        print("============================")

#Função Update
def atualizar_jogo(id_jogo, novo_nome, novo_genero, novo_preco):
    cursor.execute(
        #O 'UPDATE' é um comando SQL utilizado para atualizar registros existentes em uma tabela do db.
        "UPDATE jogos SET nome = ?, genero = ?, preco = ? WHERE id = ?", (novo_nome, novo_genero, novo_preco, id_jogo)
    )
    conexao.commit()
    if cursor.rowcount >0:
        print(f"Jogo com ID {id_jogo} atualizado com sucesso!")
    else:
        print(f"Nenhum jogo encontrado com ID {id_jogo}. Nenhuma atualização realizada.")


#Função Delete
def excluir_jogo(id_jogo):
    cursor.execute(
        #O 'DELETE' é um comando SQL utilizado para excluir registros existentes em uma tabela do db.
        "DELETE FROM jogos WHERE id = ?", (id_jogo,)
    )
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Jogo com ID {id_jogo} Excluido com sucesso!")
    else:
        print(f"Nenhum jogo encontrado com ID {id_jogo}. Nenhuma exclusão realizada.")


#A estrutura de repetição while criada abaixo, tem por finalidade manter o sistema em execução até que o usuário queira sair do sistema.
while True:
    limpar_tela()
    print('=============================')
    print("Sistema de cadastro de jogos: ")
    print('=============================')
    print('[1] - Cadastrar novo produto')
    print('[2] - listar produtos')
    print('[3] - Atualizar produto')
    print('[4] - Excluir produto')
    print('[5] - Sair do sistema')
    #o try/except abaixo está sendo utilizado para tratar possíveis erros de entrada de dados (ex: letras/caracteres ou opção inválida)
    try:
        opicao = int(input('Escolha uma opção: '))
        if opicao not in range(1, 6):
            #raise ValueError é utilizado para gerar uma exceção do tipo ValueError, 
            #que será capturada pelo bloco excepr subsequente, caso a condição seja atendida (opicao não esteja entre 1 e 5)
            raise ValueError
        
    except ValueError:
        print('Entrada invalida! Digite somente os valores acima! ')
        time.sleep(6)
        continue
    #match/case é só um switch case em python.
    match opicao:
        case 1:
            while True:
                limpar_tela()
                # Cadastrar
                print(f'--- Iniciando Cadastro de jogos ---')
                try:
                    #Validação do nome
                    nome = input("Digite o nome do Jogo que deseja Cadastrar:").strip()
                    if nome.casefold() == "abc":
                        raise ValueError ("O nome do jogo não pode ser 'abc'!")
                    if not nome:
                        raise ValueError("O nome do jogo não pode ser vazio!")
                    #Validação do gênero
                    genero = input("Digite o gênero do jogo: ").strip()
                    if genero.casefold() == "abc":
                        raise ValueError("O gênero do jogo não pode ser 'abc'!")
                    if not genero:
                        raise ValueError("O gênero do jogo não pode ser vazio!")
                    #validação do preço
                    preco_str = input("Digite o Valor do jogo: ")
                    preco = float(preco_str.replace(',', '.')) # substitui vírgula por ponto.
                    if preco <= 0:
                        raise ValueError("O preço do jogo deve ser um número maior que zero!")
                    #Se todas as validações ocorreem sem erros, o loop será interrompido e o jogo será cadastrado no sistema
                    break
                except ValueError as e:
                    #O bloco except acima está capturando a exceção ValueError e exibindo uma mensagem de erro, informando ao usuário que a entrada de dados foi inválida e solicita que ele tente novamente.
                    print(f"Erro: {e} | | Tente novamente.")
                    time.sleep(3)
            #Se tudo ocorrer sem erros, o jogo será cadastrado no sistema e uma mensagem de sucesso será exibida
            cadastrar(nome, genero, preco)
            time.sleep(3)

        case 2:
            # listar 
            print('--- Listando jogos cadastrados ---')
            listar_jogos()

        case 3:
            while True:
                limpar_tela()
                listar_jogos()
                time.sleep(6)
                limpar_tela()
                # Atualizar
                print('--- Atualizando Jogo ---')
                try:
                    id_jogo = int(input("Digite o ID do jogo que deseja atualizar: "))
                    if id_jogo <= 0:
                        raise ValueError("O ID do jogo deve ser um número maior que zero!")
                    if not cursor.execute("SELECT id FROM jogos WHERE id = ?", (id_jogo,)).fetchone():
                        raise ValueError("Nenhum jogo encontrado com o ID fornecido.")
                    novo_nome = input("Digite o novo nome do jogo:").strip()
                    if not novo_nome:
                        raise ValueError("O nome do jogo não pode ser vazio!")
                    if novo_nome.casefold() == "abc":
                        raise ValueError("O nome do jogo não pode ser 'abc'!")
                    novo_genero = input("Digite o novo gênero do jogo: ").strip()
                    if not novo_genero:
                        raise ValueError("O gênero do jogo não pode ser vazio!")
                    if novo_genero.casefold() == "abc":
                        raise ValueError("O gênero do jogo não pode ser 'abc'!")
                    novo_preco_str = input("Digite o novo preço do jogo: ")
                    novo_preco = float(novo_preco_str.replace(",", "."))
                    if novo_preco <= 0:
                        raise ValueError("O preço do jogo deve ser um número maior que zero!")
                    atualizar_jogo(id_jogo, novo_nome, novo_genero, novo_preco)
                    break
                except ValueError as e:
                    print(f"Erro: {e} | | Tente novamente.")
                    time.sleep(3)
        case 4: 
            while True:
                limpar_tela()
                # Excluindo
                print('--- Tela de exclusão de jogos ---')
                listar_jogos()
                time.sleep(3)
                try:
                    id_jogo = int(input("Digite o ID do jogo que deseja excluir:"))
                    if id_jogo <= 0:
                        raise ValueError("O ID do jogo deve ser um número maior que zero!")
                    excluir_jogo(id_jogo)
                    break
                except ValueError as e:
                    print(f"Erro: {e} | | Tente novamente.")
                    time.sleep(3)
        case 5:
            # Finalizando aplicação
            print('Saindo do sistema')
            #O 'close()' é utilizado para fechar a conexão com o banco de dados.
            conexao.close()
            break
    time.sleep(6)
        