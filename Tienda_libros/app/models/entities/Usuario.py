from werkzeug.security import generate_password_hash, check_password_hash   # uno genera y el otro permite saber si una clave ingresada en texto plano coincide con una clave encriptada
from flask_login import UserMixin


class Usuario(UserMixin):
    
    def __init__(self, id, usuario, password, tipo_usuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo_usuario = tipo_usuario
    
    
    @classmethod
    def verificar_password(self, encriptado, password):
        return check_password_hash(encriptado, password)    # pasamos el pass encriptado y el pass sin encriptar