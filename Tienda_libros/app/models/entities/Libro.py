class Libro():
    
    def __init__(self, isbn, titulo, autor, ano_edicion, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano_edicion = ano_edicion
        self.precio = precio
        self.unidades_vendidas = 0