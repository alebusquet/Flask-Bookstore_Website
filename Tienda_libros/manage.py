#from flask_script import Manager       # saque todo lo de manager porque da error --> ModuleNotFoundError: No module named 'flask._compat'
#from flask_script import Server
from app import inicializar_app         # nos retorna la aplicacion que hemos instanciado a partir de Flask
from config import config               # del archivo config importamos el diccionario


configuracion = config['development']
app = inicializar_app(configuracion)


#manager = Manager(app)                 # saque todo lo de manager porque da error --> ModuleNotFoundError: No module named 'flask._compat'
#manager.add_command('runserver', Server(host='127.0.0.1', port=5010))  # asi se cambiaria el port (ojo importar Server)

if __name__ == '__main__':
    #manager.run()                      # saque todo lo de manager porque da error --> ModuleNotFoundError: No module named 'flask._compat'
    app.run()



