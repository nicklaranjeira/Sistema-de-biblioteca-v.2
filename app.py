from funcoes import *
while True: # loop principal do sistema
    print("Escolha:\n\n1-Bibliotecário\n2-Usuário\n0-Sair\n")
    user = int(input("---->")) # entrada do usuario

    if user == 1: # acesso como bibliotecario
        os.system('cls')
        menu_bibliotecario()
    elif user == 2: # acesso como usuario
        os.system('cls')
        menu_user()
    elif user == 0: # sair do sistema
         os.system('cls')
         print('Saindo...')
         break
    else: # opcao invalida
        os.system('cls')
        print("Opção inválida tente novamente!")
