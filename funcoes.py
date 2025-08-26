from classes import *
livro = {}
livro1  = Livro(id = 1, titulo="1984", autor="George Orwell", genero="Distopia", situacao="disponível")
livro2  = Livro(id = 2,titulo="Admirável Mundo Novo", autor="Aldous Huxley", genero="Distopia", situacao="disponível")
livro3  = Livro(id = 3,titulo="Fahrenheit 451", autor="Ray Bradbury", genero="Distopia", situacao="disponível")
livro4  = Livro(id = 4,titulo="Jogos Vorazes", autor="Suzanne Collins", genero="Distopia", situacao="disponível")
livro5  = Livro(id = 5,titulo="Laranja Mecânica", autor="Anthony Burgess", genero="Distopia", situacao="disponível")

livro6  = Livro(titulo="O Hobbit", autor="J.R.R. Tolkien", genero="Fantasia", situacao="disponível")
livro7  = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", genero="Fantasia", situacao="disponível")
livro8  = Livro(titulo="As Crônicas de Nárnia", autor="C.S. Lewis", genero="Fantasia", situacao="disponível")
livro9  = Livro(titulo="Harry Potter e a Pedra Filosofal", autor="J.K. Rowling", genero="Fantasia", situacao="disponível")
livro10 = Livro(titulo="Percy Jackson e o Ladrão de Raios", autor="Rick Riordan", genero="Fantasia", situacao="disponível")

livro11 = Livro(titulo="Fundação", autor="Isaac Asimov", genero="Ficção", situacao="disponível")
livro12 = Livro(titulo="Eu, Robô", autor="Isaac Asimov", genero="Ficção", situacao="disponível")
livro13 = Livro(titulo="Neuromancer", autor="William Gibson", genero="Ficção", situacao="disponível")
livro14 = Livro(titulo="Duna", autor="Frank Herbert", genero="Ficção", situacao="disponível")
livro15 = Livro(titulo="Frankenstein", autor="Mary Shelley", genero="Ficção", situacao="disponível")

livro16 = Livro(titulo="A Revolução dos Bichos", autor="George Orwell", genero="Distopia", situacao="disponível")
livro17 = Livro(titulo="A Máquina do Tempo", autor="H.G. Wells", genero="Ficção", situacao="disponível")
livro18 = Livro(titulo="Guerra dos Mundos", autor="H.G. Wells", genero="Ficção", situacao="disponível")
livro19 = Livro(titulo="A Canção de Gelo e Fogo", autor="George R.R. Martin", genero="Fantasia", situacao="disponível")
livro20 = Livro(titulo="O Nome do Vento", autor="Patrick Rothfuss", genero="Fantasia", situacao="disponível")

livro21 = Livro(titulo="A Mão Esquerda da Escuridão", autor="Ursula K. Le Guin", genero="Ficção", situacao="disponível")
livro22 = Livro(titulo="Os Despossuídos", autor="Ursula K. Le Guin", genero="Ficção", situacao="disponível")
livro23 = Livro(titulo="O Conto da Aia", autor="Margaret Atwood", genero="Distopia", situacao="disponível")
livro24 = Livro(titulo="A Roda do Tempo", autor="Robert Jordan", genero="Fantasia", situacao="disponível")
livro25 = Livro(titulo="Mistborn", autor="Brandon Sanderson", genero="Fantasia", situacao="disponível")


livro[0]= livro1
livro[1]= livro2
livro[2]= livro3
livro[3]= livro4
livro[4]= livro5
livro[5]= livro6
livro[6]= livro7
livro[7]= livro8
livro[8]= livro9
livro[9]=livro10
livro[10]=livro11
livro[11]=livro12
livro[12]=livro13
livro[13]=livro14
livro[14]=livro15
livro[15]=livro16
livro[16]=livro17
livro[17]=livro18
livro[18]=livro19
livro[19]=livro20
livro[20]=livro21
livro[21]=livro22
livro[22]=livro23
livro[23]=livro24
livro[24]=livro25
print(livro)

def emprestar(livro):
    emprestimo = int(input("Selecione o livro que você quer emprestar:\n\n"))
    for chave, valor in livro.items():
        (print(f'{chave} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}'))

    livro_emprestado = emprestimo