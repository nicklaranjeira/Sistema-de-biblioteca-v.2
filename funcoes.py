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
livro[24] = Livroid = 25,titulo="Mistborn", autor="Brandon Sanderson", genero="Fantasia", situacao="disponível")


def emprestar(livro):
    emprestimo = int(input("Selecione o livro que você quer emprestar:\n\n"))
    for chave, valor in livro.items():
        (print(f'{chave} - {valor.getTitulo()} - {valor.getAutor()} - {valor.getGenero()} - {valor.getSituacao()}'))

    livro_emprestado = emprestimo