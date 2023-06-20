class Autor():
    
    def __init__(self, id, apellidos, nombres, fecha_nacimiento=None): # por si no tenemos la fecha
        self.id = id
        self.apellidos = apellidos
        self.nombres = nombres
        self.fecha_nacimiento = fecha_nacimiento
    
    
    def nombre_completo(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)          # para que devuelva apellido y nombre