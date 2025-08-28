from classes import *
import os
livro = {}
emprestados = []
livro[0]  = Livro(id = 1, titulo="1984", autor="George Orwell", genero="Distopia", situacao="disponível")
livro[1]  = Livro(id = 2,titulo="Admirável Mundo Novo", autor="Aldous Huxley", genero="Distopia", situacao="disponível")
livro[2]  = Livro(id = 3,titulo="Fahrenheit 451", autor="Ray Bradbury", genero="Distopia", situacao="disponível")
livro[3]  = Livro(id = 4,titulo="Jogos Vorazes", autor="Suzanne Collins", genero="Distopia", situacao="disponível")
livro[4]  = Livro(id = 5,titulo="Laranja Mecânica", autor="Anthony Burgess", genero="Distopia", situacao="disponível")
livro[5]  = Livro(id = 6,titulo="O Hobbit", autor="J.R.R. Tolkien", genero="Fantasia", situacao="disponível")
livro[6]  = Livro(id = 7,titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", genero="Fantasia", situacao="disponível")
livro[7]  = Livro(id = 8,titulo="As Crônicas de Nárnia", autor="C.S. Lewis", genero="Fantasia", situacao="disponível")
livro[8]  = Livro(id = 9,titulo="Harry Potter e a Pedra Filosofal", autor="J.K. Rowling", genero="Fantasia", situacao="disponível")
livro[9] = Livro(id = 10,titulo="Percy Jackson e o Ladrão de Raios", autor="Rick Riordan", genero="Fantasia", situacao="disponível")

livro[10] = Livro(id = 11,titulo="Fundação", autor="Isaac Asimov", genero="Ficção", situacao="disponível")
livro[11] = Livro(id = 12,titulo="Eu, Robô", autor="Isaac Asimov", genero="Ficção", situacao="disponível")
livro[12] = Livro(id = 13,titulo="Neuromancer", autor="William Gibson", genero="Ficção", situacao="disponível")
livro[13] = Livro(id = 14,titulo="Duna", autor="Frank Herbert", genero="Ficção", situacao="disponível")
livro[14] = Livro(id = 15,titulo="Frankenstein", autor="Mary Shelley", genero="Ficção", situacao="disponível")

livro[15] = Livro(id = 16,titulo="A Revolução dos Bichos", autor="George Orwell", genero="Distopia", situacao="disponível")
livro[16] = Livro(id = 17,titulo="A Máquina do Tempo", autor="H.G. Wells", genero="Ficção", situacao="disponível")
livro[17] = Livro(id = 18,titulo="Guerra dos Mundos", autor="H.G. Wells", genero="Ficção", situacao="disponível")
livro[18] = Livro(id = 19,titulo="A Canção de Gelo e Fogo", autor="George R.R. Martin", genero="Fantasia", situacao="disponível")
livro[19] = Livro(id = 20,titulo="O Nome do Vento", autor="Patrick Rothfuss", genero="Fantasia", situacao="disponível")

livro[20] = Livro(id = 21,titulo="A Mão Esquerda da Escuridão", autor="Ursula K. Le Guin", genero="Ficção", situacao="disponível")
livro[21]= Livro(id = 22,titulo="Os Despossuídos", autor="Ursula K. Le Guin", genero="Ficção", situacao="disponível")
livro[22]= Livro(id = 23,titulo="O Conto da Aia", autor="Margaret Atwood", genero="Distopia", situacao="disponível")
livro[23]= Livro(id = 24,titulo="A Roda do Tempo", autor="Robert Jordan", genero="Fantasia", situacao="disponível")
livro[24] = Livro(id = 25,titulo="Mistborn", autor="Brandon Sanderson", genero="Fantasia", situacao="disponível")


def emprestar(livro):
    print("--------Empréstimo de livro---------")
    busca = int(input("\nComo deseja buscar?\n1-Por Genêro textual \n2-Autor \n3-Todos os livros"))
    if busca == 1: 
        os.system('cls')
        listar_por_genero(livro)
    if busca == 2:
        os.system('cls')
        listar_por_autor(livro)
    if busca == 3:
        os.system('cls')
        listar_todos_livros(livro)
    empréstimo = int(input("\nDigite o Id do livro que você deseja emprestar\n----->"))
    livro[empréstimo] = livro[empréstimo].setSituacao(situacao='Emprestado')
    emprestados.append(livro[empréstimo])
    print("\nLivro emprestado com sucesso!\nPrazo máximo para devolução: 30 dias")
    back_menu()
        


def menu_listar(livro): # problema
    print("Selecione uma opção de listagem:")
    print("1 - Listar todos os livros") 
    print("2 - Listar livros por gênero")
    print("3 - Listar livros por autor")
    print("4 - Listar livros emprestados")
    print("0 - Voltar ao menu principal")
    opcao = int(input("Opção: "))
    if opcao == 1:
        os.system("cls")
        listar_todos_livros(livro)
        back_menu()
    elif opcao == 2:
        os.system("cls")
        listar_por_genero(livro)
        back_menu()
    elif opcao == 3:
        os.system("cls")
        listar_por_autor(livro)
        back_menu()
    elif opcao == 4:
        os.system("cls")
        listar_emprestados(livro)
        back_menu()
    elif opcao == 0:
        os.system("cls")
        menu_principal()
    else:
        print("Opção invalida")

def listar_todos_livros(livro):
    for id, valor in livro.items():
        print(f'{id+1} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_por_genero(livro):
    busca_genero = input("Digite o genêro da pesquisa: \n1-Distopia \n2-Fantasia \n3-Ficção\n----->")
    for id, valor in livro.items():
        if valor.getGenero() == busca_genero:
            print(f'{id+1} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_por_autor(livro):
    busca_autor = input("Autor:")
    for id, valor in livro.items():
        if valor.getAutor() == busca_autor:
            print(f'{id+1} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_emprestados(livro):
    for id, valor in livro.items():
        if valor.getSituacao() == "emprestado":
            print(f'{id+1} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def remover_livro(livro,id):
    print("Selecione uma opção: ")
    print("1- Apagar livro")
    print("0- Voltar ao menu principal")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_todos_livros(livro)
        id = int(input("Qual o id do livro que você deseja remover?"))
        livro.pop(id, None)
    elif opcao == 0:
        return
    else:
        print("Opção inválida.")

def adicionar_livro(livro):
    print("Selecione uma opção: ")
    print("1- Adicionar livro")
    print("0- Voltar ao menu principal")
    opcao = int(input("Opção: "))
    if opcao == 1:       
        id = len(livro)+1
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        genero = input("Gênero do livro: ")
        situacao = "disponível"
        livro[id] = Livro(id, titulo, autor, genero, situacao)
        print("Livro adicionado com sucesso.")
    elif opcao == 0:
        return
    else:
        print("Opção inválida.")

def editar_livro(livro):
    print("Livros da biblioteca:")
    print(listar_todos_livros(livro))
    print("Digite o Id do livro que você deseja atualizar:")
    escolha = int(input("\n->"))
    print("O que você deseja atualizar?\n1. Título \n2. Autor \n3. Gênero \n4. Situação")
    atualizar= int(input("\n->"))
    if atualizar == 1:
        novo_titulo = input("Digite o novo título:")
        livro[escolha].setTitulo(novo_titulo)
    elif atualizar == 2:
        novo_autor = input("Digite o novo autor:")
        livro[escolha].setAutor(novo_autor)
    elif atualizar == 3:
        novo_genero = input("Digite o novo gênero:")
        livro[escolha].setGenero(novo_genero)
    elif atualizar == 4:
        nova_situacao = input("Digite a nova situação:")
        livro[escolha].setSituacao(nova_situacao)
    else:
        print ("Opção invalida, tente novamente")
        os.system("pause")

def devolver():
    print('Devolução de livro:\n')
    id_devolucao = int(input("Digite aqui o id do livro que deseja devolver\n----->"))
    livro[id_devolucao] = livro[id_devolucao].setSituacao(situacao='Disponivel')
    emprestados.pop(livro[id_devolucao])
    print("Livro devolvido com sucesso!")
    back_menu()

def con_emprestados():
    print("Consulta de livros emprestados\n: ")
    for i in range(len(emprestados)):
        print(f'{i+1} {emprestados[i]}')

def menu_principal():
    while True:
        print("BEM VINDO AO SISTEMA DA BIBLIOTECA\n")
        print("Selecione a opção que deseja:")
        print("1 - Listar livros")
        print("2 - Adicionar livro")
        print("3 - Remover livro")
        print("4 - Editar livro")
        print("5 - Emprestar livro")
        print("6 - Devolver livro")
        print("7-  Consultar livros emprestados")
        print("0 - Sair")
        opcao = int(input("Opção: "))

        if opcao == 1:
            os.system('cls')
            menu_listar(livro)
        elif opcao == 2:
            os.system('cls')
            adicionar_livro(livro)
        elif opcao == 3:
            os.system('cls')
            remover_livro(livro, None)  
        elif opcao == 4:
            os.system('cls')
            editar_livro(livro)
        elif opcao == 5:
            os.system('cls')
            emprestar(livro)
        elif opcao ==6:
            os.system("cls")
            devolver()
        elif opcao ==7:
            os.system('cls')
            con_emprestados()
        elif opcao == 0:
            os.system('cls')
            print("Saindo...")
            os.system('pause')
            break
        else:
            print("Opção inválida.")
            continue

def back_menu():
    back_menu = int(input("\nPressione 1 para voltar ao menu e 0 para sair do sistema\n---->"))
    if back_menu == 1:
        menu_principal()
    if back_menu == 2:
        print("Saindo...")
        os.system("cls")
        os.system('pause')