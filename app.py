import os
from funcoes import *
from classes import *

while True:
    print("Escolha:\n\n1-Bibliotecário\n2-Usuário\n0-Sair\n")
    user = int(input("---->"))
    if user == 1:
        os.system('cls')
        menu_bibliotecario()
    elif user == 2:
            os.system('cls')
            menu_user()
    elif user == 0:
         os.system('cls')
         print('Saindo...')
         os.system('cls')
         break
    else:
        os.system('cls')
        print("Opção inválida tente novamente!")
