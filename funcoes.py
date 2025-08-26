from classes import *
livros = [
    ("Dom Casmurro", "Machado de Assis", "Romance"),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance"),
    ("Vidas Secas", "Graciliano Ramos", "Drama"),
    ("Grande Sertão: Veredas", "Guimarães Rosa", "Romance"),
    ("O Cortiço", "Aluísio Azevedo", "Romance"),
    ("A Hora da Estrela", "Clarice Lispector", "Ficção"),
    ("Macunaíma", "Mário de Andrade", "Modernismo"),
    ("Iracema", "José de Alencar", "Romance"),
    ("Senhora", "José de Alencar", "Romance"),
    ("O Guarani", "José de Alencar", "Romance"),
    ("O Ateneu", "Raul Pompeia", "Romance"),
    ("Os Maias", "Eça de Queirós", "Romance"),
    ("O Primo Basílio", "Eça de Queirós", "Romance"),
    ("Dom Quixote", "Miguel de Cervantes", "Clássico"),
    ("1984", "George Orwell", "Distopia"),
    ("Admirável Mundo Novo", "Aldous Huxley", "Distopia"),
    ("Fahrenheit 451", "Ray Bradbury", "Distopia"),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia"),
    ("O Hobbit", "J.R.R. Tolkien", "Fantasia"),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia"),
    ("Orgulho e Preconceito", "Jane Austen", "Romance"),
    ("Drácula", "Bram Stoker", "Terror"),
    ("Frankenstein", "Mary Shelley", "Terror"),
    ("A Moreninha", "Joaquim Manuel de Macedo", "Romance"),
    ("Capitães da Areia", "Jorge Amado", "Drama")
]
livros = [Livro(titulo, autor, genero) for titulo, autor, genero in livros]
