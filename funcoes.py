from classes import *
livro = {}
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
    busca = int(input("Como deseja buscar?\n1-Por Genêro textual\n2-Autor\n3-Todos os livros"))
    if busca == 1: 
        listar_por_genero(livro)
    if busca == 2:
        listar_por_autor(livro)
    if busca == 3:
        listar_todos_livros(livro)
    empréstimo = int(input("Digite o Id do livro que você deseja emprestar\n----->"))
    livro[empréstimo] = livro[empréstimo].setSituacao(Situacao='Emprestado')


def menu_listar(livro):
    print("Selecione uma opção de listagem:")
    print("1 - Listar todos os livros")
    print("2 - Listar livros por gênero")
    print("3 - Listar livros por autor")
    print("4 - Listar livros emprestados")
    print("0 - Voltar ao menu principal")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_todos_livros(livro)
    elif opcao == 2:
        genero = input("Digite o gênero: ")
        listar_por_genero(livro, genero)
    elif opcao == 3:
        autor = input("Digite o autor: ")
        listar_por_autor(livro, autor)
    elif opcao == 4:
        listar_emprestados(livro)
    elif opcao == 0:
        return
    else:
        print("Opção invalida")

def listar_todos_livros(livro):
    for id, valor in livro.items():
        print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_por_genero(livro):
    busca_genero = int(input("Escolha o genêro da pesquisa: \n1-Distopia\2-Fantasia\3-Ficção"))
    for id, valor in livro.items():
        if valor.getGenero() == busca_genero:
            print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_por_autor(livro):
    busca_autor = input("Autor:")
    for id, valor in livro.items():
        if valor.getAutor() == busca_autor:
            print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_emprestados(livro):
    for id, valor in livro.items():
        if valor.getSituacao() == "emprestado":
            print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

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
        id = int(input("ID do livro: "))
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
    pass
