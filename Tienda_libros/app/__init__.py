from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from .models.ModeloCompra import ModeloCompra
from .models.ModeloLibro import ModeloLibro
from .models.ModeloUsuario import ModeloUsuario

from  .models.entities.Compra import Compra
from  .models.entities.Libro import Libro
from  .models.entities.Usuario import Usuario

from .consts import *

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)                 # paso la aplicacion sobre la cual va a tener efecto y permitira que se conecte
login_manager_app = LoginManager(app)   # crea un administrador de Login para nuestra app


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        usuario = Usuario(None, request.form ['usuario'], request.form ['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        
        if usuario_logeado != None:
            login_user(usuario_logeado)                 # permite logear al usuario
            flash(MENSAJE_BIENVENIDA, 'success')
            return redirect(url_for('index'))           # importarlas!!
        else:
            flash(LOGIN_CREDENCIALESINVALIDAS, 'warning')
            return render_template('auth/login.html')
        
    else:
        return render_template('auth/login.html')



@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))



@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipo_usuario.id == 1:
            try:
                libros_vendidos = ModeloLibro.listar_libros_vendidos(db)
                data = {
                    'titulo': 'Libros Vendidos',
                    'libros_vendidos': libros_vendidos
                }
                return render_template('index.html', data=data)
            except Exception as ex:
                return render_template('errores/error.html', mensaje=format(ex))
        else:
            try:
                compras = ModeloCompra.listar_compras_usuario(db, current_user)
                data = {
                    'titulo': 'Mis compras',
                    'compras': compras
                }
                return render_template('index.html', data=data)
            except Exception as ex:
                return render_template('errores/error.html', mensaje=format(ex))
    else:
        return redirect(url_for('login'))



@app.route('/libros')
@login_required
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)      # llama al proceso del modelo para que lo ejecute
        data = {
            'titulo': 'Listado de libros',
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        return render_template('errores/error.html', mensaje=format(ex))



@app.route('/comprarLibro', methods=['POST'])
@login_required
def comprarlibro():
    data_request = request.get_json()
    data= {}
    try:
        libro = Libro(data_request['isbn'], None, None, None, None)
        compra = Compra(None, libro, current_user)
        data['exito'] = ModeloCompra.registrar_compra(db, compra)
    except Exception as ex:
        data['mensaje'] = format(ex)
        data['exito'] = False
    return jsonify(data)


# Control del Error 404 para Pagina no encontrada
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404    # para renderzar la plantilla. Se pasa la ubicacion de la plantilla y el tipo de error --> 404


# Control del Error 401 para Pagina no autorizada
def pagina_no_autorizada(error):
    return redirect(url_for('login'))


def inicializar_app(config):                # estas lineas dejarlas siempre al final. Con (Config) en el parametro se indica que recibe una configuracion
    app.config.from_object(config)          # indica que la app obtendra la configuracion de un objeto

    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)   # para el error 404, la vista que sera lanzada es 'pagina_no_encontrada'
    app.register_error_handler(401, pagina_no_autorizada)
    return app                              # nos retorna la aplicacion que hemos instanciado a partir de Flask



# Para que el navegador no tome info del cache, sino que haga un reload de la pagina siempre!!
@app.after_request
def add_cache_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
