from .entities.Autor import Autor
from .entities.Libro import Libro

class ModeloLibro():
    
    @classmethod                            # defino como decorador de clase para poder usarlo sin crear una instancia de la clase ModeloLibro
    def listar_libros(self, db):            # db es la variable que usamos para las conexiones
        try:
            cursor = db.connection.cursor()
            sql = """SELECT LIB.isbn, LIB.titulo, LIB.ano_edicion, LIB.precio,
                    AUT.apellidos, AUT.nombres
                    FROM libro LIB JOIN autor AUT ON LIB.autor_id = AUT.id 
                    ORDER BY LIB.titulo ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()        # sabemos que aca estan todos los datos a modo de tupla
            
            libros = []
            for row in data:
                aut = Autor(0, row[4], row[5])      # creamos instancia de la clase autor (ojo importar Autor)
                lib = Libro(row[0], row[1], aut, row[2], row[3])    # creamos instancia de la clase libro (ojo importar Libro)
                libros.append(lib)
            return libros
        
        except Exception as ex:             # Esto es para capturar el error, si existe
            raise Exception(ex)


    @classmethod                            # defino como decorador de clase para poder usarlo sin crear una instancia de la clase ModeloLibro
    def listar_libros_vendidos(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT COM.libro_isbn, LIB.titulo, LIB.precio,
                    COUNT(COM.libro_isbn) AS Unidades_Vendidas
                    FROM compra COM JOIN libro LIB ON COM.libro_isbn = LIB.isbn
                    GROUP BY COM.libro_isbn ORDER BY 4 DESC, 2 ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()        # sabemos que aca estan todos los datos a modo de tupla
            libros = []
            for row in data:
                lib = Libro(row[0], row[1], None, None, row[2])    # creamos instancia de la clase libro (ojo importar Libro)
                lib.unidades_vendidas = int(row[3])
                libros.append(lib)
            return libros
        
        except Exception as ex:
            raise Exception(ex)