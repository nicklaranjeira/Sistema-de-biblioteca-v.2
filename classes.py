class Livros:
    def __init__(self, titulo, autor, genero, disponivel):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__disponivel= disponivel

    # ----------------------------------------------------------------------
# Metódos GETS and SETs 
#GETs

def getTitulo(self):
    return self.__titulo

def getAutor(self):
    return self.__autor

def getGenero(self):
    return self.__genero

def getDisponivel(self):
    return self.__disponivel

#SETs 
def setTitulo(self,titulo):
    self.__titulo = titulo
    return self.__titulo

def setAutor(self,autor):
    self.__autor = autor
    return self.__autor

def setGenero(self,genero):
    self.__genero = genero
    return self.__genero

def setDisponivel(self,disponivel):
    self.__disponivel = disponivel
    return self.__disponivel
