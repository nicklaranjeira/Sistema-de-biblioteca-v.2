class Livro: # metodo construtor, inicializa os atributos do livro
    def __init__(self,id, titulo, autor, genero, situacao="Disponível"):
        self.id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__situacao = situacao

    # metodos get (acessar os dados)
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getGenero(self):
        return self.__genero

    def getSituacao(self):
        return self.__situacao
    
    def getId(self):
        return self.__id

    # metodo set (altera os dados)
    def setTitulo(self, titulo):
        self.__titulo = titulo
        return titulo

    def setAutor(self, autor):
        self.__autor = autor
        return autor

    def setGenero(self, genero):
        self.__genero = genero
        return genero

    def setSituacao(self, situacao):
        self.__situacao = situacao
        return situacao

    def setId(self, id):
        self.__id = id
        return id