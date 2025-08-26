class Livro:
    def __init__(self,id, titulo, autor, genero, situacao="Disponível"):
        self.id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__situacao = situacao

    # 
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

    # 
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setGenero(self, genero):
        self.__genero = genero

    def setSituacao(self, situacao):
        self.__situacao = situacao