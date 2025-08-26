import os
from funcoes import *

while True:
    print("Bem-vindo ao sistema de biblioteca!")
    print("Selecione a opção que deseja:")
    print("1 - Listar livros")
    print("2 - Adicionar livro")
    print("3 - Remover livro")
    print("4 - Editar livro")
    print("5 - Emprestar livro")
    print("6 - Devolver livro")
    print("0 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        menu_listar(livro)
    elif opcao == 2:
        adicionar_livro(livro)
    elif opcao == 3:
        remover_livro(livro, None)  
    elif opcao == 4:
        editar_livro(livro)
    elif opcao == 5:
        emprestar()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        continue
