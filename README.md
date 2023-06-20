# Librería en línea, confeccionada con Python y Flask

## Mediante esta librería se puede:
* Ingresar mediante validación de credenciales

* Categorización de usuarios en Clientes y Administrador

* Desde Cliente:
  * Visualización de libros disponibles
  * Posibilidad de compra de libros

* Desde Administrador:
  * Seguimiento de libros vendidos
  * Total de ingresos por libro y por total

* Logout del sistema

-----
-----

### Implementación de las tecnologías necesarias

1.	Creación del entorno de trabajo:
    
    Clonar el repositorio
    
    Creación del entorno virtual: `python3 -m venv venv-Flask`
    
    Activación del entorno: `source venv-Flask/bin/activate`
    
    Instalación de librerías mediante el archivo requirements.txt: `pip install -r requirements.txt`
    
    Una vez contamos con estos pasos previos, se activa el server de Flask para poder acceder a la aplicación mediante el “localhost”: `python manage.py runserver`.
    
    En el navegador, en la dirección http://127.0.0.1:5000/login se puede acceder a la aplicación, como puede verse abajo:

  	![Captura de pantalla 2023-06-20 a las 03 47 59](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/69c52c44-fb6b-4949-9701-1acc3fb1b966)

3.	Activacion de MariaDB:

  	Descarga e instalacion de XAMPP (Apache + MariaDB + PHP + Perl)

  	En Aplicaciones, carpeta XAMPP, correr el “manager-osx”

  	Se abre una ventana con el controlador de servers de phpMyAdmin

  	Dar “Start” a todos los Servers. Puede ser necesario cambiar el puerto por default del Server “MySQL Database”, que es el 3306 y suele ser usado por MySQL. En mi caso lo cambie al 3308.
  	
  	![Captura de pantalla 2023-06-20 a las 03 56 38](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/0f62776e-d17e-4240-a048-8b5c2314f069)

  	Boton “Go to application”:
  	
  	![Captura de pantalla 2023-06-20 a las 03 57 31](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/ab441186-8152-4a04-87b4-b01ffa866c85)

  	Click en “phpMyAdmin”:

  	![Captura de pantalla 2023-06-20 a las 03 59 32](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/6406ac69-b1d5-40af-b497-a581ffa6cdc8)

  	Ingresando el “Usuario” y la “Contraseña” finalmente se accede a la aplicación:

  	![Captura de pantalla 2023-06-20 a las 04 00 46](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/0e030fea-bc5d-4d23-8ff6-211686408c53)

  	Aquí vemos la estructura de “Tienda_Libros”, la base de datos que cree en MariaDB (imagen). Mediante ella puedo ir siguiendo distintos aspectos como los autores, el listado de libros, los nombres y las categorias de los usuarios y los libros que ya han sido comprados.

  	![Captura de pantalla 2023-06-20 a las 04 02 14](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/929b1225-e59b-4b63-b943-be3989415923)

-------

### De esta manera tenemos activo:
* El entorno virtual con sus librerias
* El server que permite tener activa la base de datos en MariaDB
* El server Flask que nos permite correr la aplicación en localhost

-------

### Funcionalidades de la aplicación en Flask
