import os
from funcoes import *
from classes import *

print("Escolha:\n1-Bibliotecário\n2-Usuário")
user = int(input("---->"))
if user == 1:
    menu_bibliotecario()
if user == 2:
        menu_user()
