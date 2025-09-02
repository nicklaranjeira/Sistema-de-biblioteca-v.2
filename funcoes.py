from classes import * #importa as classes 
import os
livro = {} # no dicionario a chave é o ID e o valor é um objeto da classe Livro.

livro[1]  = Livro(id = 1, titulo="1984", autor="George Orwell", genero="Distopia", situacao="disponível")
livro[2]  = Livro(id = 2,titulo="Admirável Mundo Novo", autor="Aldous Huxley", genero="Distopia", situacao="disponível")
livro[3]  = Livro(id = 3,titulo="Fahrenheit 451", autor="Ray Bradbury", genero="Distopia", situacao="disponível")
livro[4]  = Livro(id = 4,titulo="Jogos Vorazes", autor="Suzanne Collins", genero="Distopia", situacao="disponível")
livro[5]  = Livro(id = 5,titulo="Laranja Mecânica", autor="Anthony Burgess", genero="Distopia", situacao="disponível")
livro[6]  = Livro(id = 6,titulo="O Hobbit", autor="J.R.R. Tolkien", genero="Fantasia", situacao="disponível")
livro[7]  = Livro(id = 7,titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", genero="Fantasia", situacao="disponível")
livro[8]  = Livro(id = 8,titulo="As Crônicas de Nárnia", autor="C.S. Lewis", genero="Fantasia", situacao="disponível")
livro[9]  = Livro(id = 9,titulo="Harry Potter e a Pedra Filosofal", autor="J.K. Rowling", genero="Fantasia", situacao="disponível")
livro[10] = Livro(id = 10,titulo="Percy Jackson e o Ladrão de Raios", autor="Rick Riordan", genero="Fantasia", situacao="disponível")

livro[11] = Livro(id = 11,titulo="Fundação", autor="Isaac Asimov", genero="Ficção", situacao="disponível")
livro[12] = Livro(id = 12,titulo="Eu, Robô", autor="Isaac Asimov", genero="Ficção", situacao="disponível")
livro[13] = Livro(id = 13,titulo="Neuromancer", autor="William Gibson", genero="Ficção", situacao="disponível")
livro[14] = Livro(id = 14,titulo="Duna", autor="Frank Herbert", genero="Ficção", situacao="disponível")
livro[15] = Livro(id = 15,titulo="Frankenstein", autor="Mary Shelley", genero="Ficção", situacao="disponível")

livro[16] = Livro(id = 16,titulo="A Revolução dos Bichos", autor="George Orwell", genero="Distopia", situacao="disponível")
livro[17] = Livro(id = 17,titulo="A Máquina do Tempo", autor="H.G. Wells", genero="Ficção", situacao="disponível")
livro[18] = Livro(id = 18,titulo="Guerra dos Mundos", autor="H.G. Wells", genero="Ficção", situacao="disponível")
livro[19] = Livro(id = 19,titulo="A Canção de Gelo e Fogo", autor="George R.R. Martin", genero="Fantasia", situacao="disponível")
livro[20] = Livro(id = 20,titulo="O Nome do Vento", autor="Patrick Rothfuss", genero="Fantasia", situacao="disponível")

livro[21] = Livro(id = 21,titulo="A Mão Esquerda da Escuridão", autor="Ursula K. Le Guin", genero="Ficção", situacao="disponível")
livro[22]= Livro(id = 22,titulo="Os Despossuídos", autor="Ursula K. Le Guin", genero="Ficção", situacao="disponível")
livro[23]= Livro(id = 23,titulo="O Conto da Aia", autor="Margaret Atwood", genero="Distopia", situacao="disponível")
livro[24]= Livro(id = 24,titulo="A Roda do Tempo", autor="Robert Jordan", genero="Fantasia", situacao="disponível")
livro[25] = Livro(id = 25,titulo="Mistborn", autor="Brandon Sanderson", genero="Fantasia", situacao="disponível")



def emprestar(livro): #função para emprestar os livros
        print("-------- Empréstimo de livro ---------")
        busca = int(input("\nComo deseja buscar?\n1-Por Genêro textual \n2-Autor \n3-Todos os livros\n----->"))
        if busca == 1: 
            os.system('cls')
            listar_por_genero(livro) #chama a função listar_por_genero
        elif busca == 2:
            os.system('cls')
            listar_por_autor(livro) #chama a função listar_por_autor
        elif busca == 3:
            os.system('cls')
            listar_todos_livros(livro) #chama a função listar_todos_livros
        else:
            os.system('cls')
            print("Opção inválida.")
            emprestar(livro) #chama a função emprestar, retorna ao inicio

        empréstimo = int(input("\nDigite o Id do livro que você deseja emprestar:\n----->")) #solicita ID do livro para empréstimo

        if empréstimo not in livro: # not in: operador de associação serve apenas para sequências, listas ou dicts
            os.system("cls")
            print("Esse id não corresponde a nenhum item da lista!\n")
            emprestar(livro) #chama a função emprestar, retorna ao inicio

        if livro[empréstimo].getSituacao() == 'Emprestado': #se o livro com o ID informado estiver 'Emprestado', retorna a função emprestar
            os.system("cls")
            print("Este livro já está emprestado! Escolha outra obra.\n\n\n")
            emprestar(livro)

        if livro[empréstimo].getSituacao() == "disponível": #se o livro com o ID informado estiver 'disponível', ele altera a situação usando SET
            livro[empréstimo].setSituacao(situacao='Emprestado')
            os.system('cls')
            print(f"\nLivro {livro[empréstimo].getTitulo()} emprestado com sucesso!\nPrazo máximo para devolução: 30 dias") #retorna o nome do livro
        back_menu_user() #retorna ao menu do usuario 
        

def menu_listar_bi(livro): #função de listagem do bibliotecario
    print("Selecione uma opção de listagem:")
    print("1 - Listar todos os livros") 
    print("2 - Listar livros por gênero")
    print("3 - Listar livros por autor")
    print("4 - Listar livros emprestados")
    opcao = int(input("Opção: "))
    if opcao == 1:
        os.system("cls")
        listar_todos_livros(livro) #chama a função listar_todos_livros
    elif opcao == 2:
        os.system("cls")
        listar_por_genero(livro) #chama a função listar_por_genero
    elif opcao == 3:
        os.system("cls")
        listar_por_autor(livro) #chama a função listar_por_autor
    elif opcao == 4:
        os.system("cls")
        listar_emprestados(livro) #chama a função listar_emprestados
    else:
        os.system('cls')
        print("Opção inválida")
        menu_listar_bi(livro) #retorna a função listar do bibliotecaro
    back_menu_bibliotecario() #retorna a função menu do bibliotecario

def menu_listar_us(livro): #função de listar livros para o usuario 
    print("Selecione uma opção de listagem:")
    print("1 - Listar todos os livros") 
    print("2 - Listar livros por gênero")
    print("3 - Listar livros por autor")
    print("4 - Listar livros emprestados")
    opcao = input("Opção: ")
    if opcao == '1':
        os.system("cls")
        listar_todos_livros(livro) #chama a função listar_todos_livros
    elif opcao == '2':
        os.system("cls")
        listar_por_genero(livro) #chama a função listar_por_genero
    elif opcao == '3':
        os.system("cls")
        listar_por_autor(livro) #chama a função listar_por_autor
    elif opcao == '4':
        os.system("cls")
        listar_emprestados(livro) #chama a função listar_emprestados
    else:
        os.system("cls")
        print("Opção inválida")
        menu_listar_us(livro) #retorna a função listar
    back_menu_user() #retorna o menu do usuario


def listar_todos_livros(livro): #função de listar
    for id, valor in livro.items(): #lista o id, nome, autor, genero e situação
        print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_por_genero(livro): #função de listar por genero
    busca_genero = input("DIGITE o genêro da pesquisa: \n1-Distopia \n2-Fantasia \n3-Ficção\n----->").capitalize() #atribui uma variavel para facilitar a busca
    os.system('cls')
    for id, valor in livro.items():
        if valor.getGenero() == busca_genero: #lista os valores que o genero é igual o valor da variavel
            print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')
        else:
            print("Opção inválida!\n")
            listar_por_genero(livro)

def listar_por_autor(livro): #função de listar por autor 
    busca_autor = input("Autor:").title()
    #os.system('cls')
    for id, valor in livro.items():
        if valor.getAutor() == busca_autor: #lista os valores que o autor é igual o informado
            print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def listar_emprestados(livro): #função de listar livros emprestados
    os.system('cls')
    for id, valor in livro.items():
        if valor.getSituacao() == "Emprestado": #lista os valores que a situação é = a "Emprestado"
            print(f'{id} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}')

def remover_livro(livro): #função de remover livros
    print("Remover um livro do sistema: ")
    listar_todos_livros(livro) #lista todos os livros
    id = int(input("\nQual o id do livro que você deseja remover?\n--->"))

    if id not in livro: #se o valor da variavel não for encontrado consta como errado, operador not in
        print("Você digitou o id errado! Digite novamente")
        remover_livro(livro) #retorna a função
    else:
        os.system("cls")
        print(f"Livro {livro[id].getTitulo()} removido!") #printa o livro indicado
        livro.pop(id) #remove o livro do dicionario livros, usando o valor da variavel id
    back_menu_bibliotecario() #retorna a função para voltar pro menu do bibliotecario 

def adicionar_livro(livro): #função adicionar livro 
    print("Adicionar um livro:\n")
    id = len(livro)+1 #+1 para que o id comece sempre em 1
    titulo = input("Título do livro: ").capitalize()
    autor = input("Autor do livro: ").capitalize()
    genero = input("Gênero do livro: ").capitalize()
    situacao = "disponível"
    livro[id] = Livro(id, titulo, autor, genero, situacao) #cria um objeto da classe Livro, armazenado dentro do dicionario livro
    os.system('cls')
    print(f"Livro {livro[id].getTitulo()} - {livro[id].getAutor()} - {livro[id].getGenero()} adicionado com sucesso.\n") #printa o livro adicionado
    back_menu_bibliotecario() #retorna a função menu do bibliotecario 
        
def editar_livro(livro):
    # funcao para editar os dados de um livro existente
    print("Livros da biblioteca:")
    listar_todos_livros(livro)  # lista todos os livros para o usuario escolher
    print("\nDigite o Id do livro que você deseja atualizar:")
    escolha = int(input("\n->"))
    if escolha not in livro:  # verifica se o id existe
        os.system('cls')
        print("Você digitou o id errado! Tente novamente")
        editar_livro(livro)  # chama a funcao novamente em caso de erro
    else:
        os.system('cls')
        print("O que você deseja atualizar?\n1. Título \n2. Autor \n3. Gênero \n4. Situação")
        atualizar= input("\n->")
        if atualizar == '1':
                novo_titulo = input("Digite o novo título:").capitalize()  # solicita novo titulo
                livro[escolha].setTitulo(novo_titulo)
                os.system('cls')
                print(f"Título alterado para: {livro[escolha].getTitulo()}.")
        elif atualizar == '2':
                novo_autor = input("Digite o novo autor:").capitalize()  # solicita novo autor
                livro[escolha].setAutor(novo_autor)
                os.system('cls')
                print(f"Autor do livro {livro[escolha].getTitulo()} alterado para {livro[escolha].getAutor()}.")
        elif atualizar == '3':
                novo_genero = input("Digite o novo gênero:").capitalize()  # solicita novo genero
                livro[escolha].setGenero(novo_genero)
                os.system('cls')
                print(f"Genêro do livro {livro[escolha].getTitulo()} alterado para {livro[escolha].getGenero()}. ")
        elif atualizar == '4':
                nova_situacao = input("Digite a nova situação:").capitalize()  # solicita nova situacao
                livro[escolha].setSituacao(nova_situacao)
                if nova_situacao == "Emprestado":  # caso seja emprestado, atualiza
                    livro[escolha].setSituacao(situacao="Emprestado")
                    os.system('cls')
                    print(f"Situação do livro {livro[escolha].getTitulo()} atualizada para {livro[escolha].getSituacao()}!")
        else:
            os.system("cls")
            print ("Opção inválida, tente novamente!\n")
            editar_livro(livro)
        back_menu_bibliotecario()  # retorna ao menu do bibliotecario

def devolver():
    # funcao para devolver um livro emprestado
    print('Devolução de livro:\n')
    id_devolucao = int(input("Digite aqui o id do livro que deseja devolver\n----->"))

    if id_devolucao not in livro:  # se id nao existe
        os.system("cls")
        print("Você digitou um id inexistente! Tente novamente")
        devolver()

    elif livro[id_devolucao].getSituacao() == "disponível":  # se ja esta disponivel
        os.system("cls")
        print("Você digitou o Id errado, tente novamente!\n")
        sair = int(input("Deseja retornar ao menu?\n1-Sim\n2-Não\n---> "))
        if sair == 1:
            back_menu_user()
        if sair == 2:
            os.system('cls')
            devolver()

    elif livro[id_devolucao].getSituacao() == "Emprestado":  # se esta emprestado devolve
         livro[id_devolucao].setSituacao(situacao='disponivel')
         os.system('cls')
         print(f"Livro {livro[id_devolucao].getTitulo()} devolvido!")
    back_menu_user()  # retorna ao menu usuario

def menu_user():
    # menu principal do usuario
    while True:
        print("BEM VINDO AO SISTEMA DA BIBLIOTECA\n")
        print("Selecione a opção que deseja:")
        print("1 - Ver livros")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("0 - Sair")
        opcao = input("\nOpção: ")

        if opcao == '1':
            os.system('cls')
            menu_listar_us(livro)  # lista livros para usuario
        elif opcao == '2':
            os.system('cls')
            emprestar(livro)  # emprestar livro
        elif opcao == '3':
            os.system('cls')
            devolver()  # devolver livro
        elif opcao == '0':
            os.system('cls')
            print("Saindo...")
            os.system('Pause')
            break
        else:
            os.system('cls')
            print("Opção inválida.")
            continue
        break

def menu_bibliotecario():
    # menu principal do bibliotecario
    while True:
        print("BEM VINDO AO SISTEMA DA BIBLIOTECA\n")
        print("Selecione a opção que deseja:")
        print("1 - Ver livros")
        print("2 - Adicionar livro")
        print("3 - Remover livro")
        print("4 - Editar livro")
        print("0 - Sair")
        opcao = input("\nOpção: ")

        if opcao == '1':
            os.system('cls')
            menu_listar_bi(livro)  # listar livros
        elif opcao == '2':
            os.system('cls')
            adicionar_livro(livro)  # adicionar livro
        elif opcao == '3':
            os.system('cls')
            remover_livro(livro)  # remover livro
        elif opcao == '4':
            os.system('cls')
            editar_livro(livro)  # editar livro
        elif opcao == '0':
            os.system('cls')
            print("Saindo...")
            os.system('Pause')
            break
        else:
            os.system('cls')
            print("Opção inválida.")
            continue
        break

def back_menu_user():
    # retorna ao menu usuario ou sai
    while True:
        retorno = int(input("\nPressione 1 para voltar ao menu ou 0 para sair do sistema\n---->"))
        if retorno == 1:
            os.system('cls')
            menu_user()
            break
        if retorno == 0:
            print("Saindo...")
            os.system("cls")
            os.system('pause')
            break
        else:
            os.system('cls')
            print("Opção inválida")
            menu_user()

def back_menu_bibliotecario():
    # retorna ao menu bibliotecario ou sai
    while True:
        retorno = int(input("\nPressione 1 para voltar ao menu ou 0 para sair do sistema\n---->"))
        if retorno == 1:
            os.system('cls')
            menu_bibliotecario()
            break
        if retorno == 0:
            print("Saindo...")
            os.system("cls")
            os.system('pause')
            break
        else:
            os.system('cls')
            print("Opção inválida")
            back_menu_bibliotecario()
