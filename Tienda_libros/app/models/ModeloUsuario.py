from .entities.Usuario import Usuario
from .entities.Tipo_Usuario import Tipo_Usuario

class ModeloUsuario():
    
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, usuario, password FROM 
                    usuario WHERE usuario = '{0}'""".format(usuario.usuario)   # a las llaves llega el nombre de usuario que se ingrese por pantalla
            cursor.execute(sql)
            data = cursor.fetchone()        # no es fetchall porque esperamos un unico registro
            if data != None:
                coincide = Usuario.verificar_password(data[2], usuario.password)
                if coincide:
                    usuario_logeado = Usuario(data[0], data[1], None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None
        
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.usuario, TIP.id, TIP.nombre 
                    FROM usuario USU JOIN tipo_usuario TIP ON USU.tipo_usuario_id = TIP.id 
                    WHERE USU.id = {0}""".format(id)   # a las llaves llega el nombre de usuario que se ingrese por pantalla
            cursor.execute(sql)
            data = cursor.fetchone()        # no es fetchall porque esperamos un unico registro
            tipo_usuario = Tipo_Usuario(data[2], data[3])
            usuario_logeado = Usuario(data[0], data[1], None, tipo_usuario)
            return usuario_logeado
        
        except Exception as ex:
            raise Exception(ex)        