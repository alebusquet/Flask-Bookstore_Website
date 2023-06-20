
class Config:
    SECRET_KEY='blasarasablabla'



# Clase para la configuracion de desarrollo
class DevelopmentConfig(Config):        # hereda de Config
    DEBUG=True                          # para que funcione, tengo que agregar la funcion en el 'init.py', inicializar_app
    
    MYSQL_HOST = '127.0.0.1'            # es donde corre la instancia. Yo le pongo la direccion porque con localhost, que es lo habitual, da error
    MYSQL_PORT = 3308                   # esto lo agrego yo y si se saca da error, porque busca en el puerto por default que es el 3306
    MYSQL_USER = 'root'                 # root tiene acceso a localhost
    MYSQL_PASSWORD = '123456'           # si tuviera un pass, iria aca entre comillas
    MYSQL_DB = 'Tienda_libros'          # el nombre de mi base de datos



config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}