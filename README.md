# Librería en línea, confeccionada con Python y Flask

## Mediante esta librería se puede:
* Ingresar mediante validación de credenciales

* Categorización de usuarios en Clientes y Administrador

* Desde Cliente:
  * Visualización de libros disponibles
  * Posibilidad de compra de libros
  * Visualización de mis libros comprados

* Desde Administrador:
  * Seguimiento de libros vendidos
  * Total de ingresos por cada libro
  * Total de ingresos por el total de libros vendidos

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

2.	Activacion de MariaDB:

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

  	![Captura de pantalla 2023-06-20 a las 11 01 29](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/dba740c9-9b25-405f-b50c-6627fb073300)

  	Aquí vemos la estructura de “Tienda_Libros”, la base de datos que cree en MariaDB (imagen). Mediante ella puedo ir siguiendo distintos aspectos como los autores, el listado de libros, los nombres y las categorias de los usuarios y los libros que ya han sido comprados.

  	![Captura de pantalla 2023-06-20 a las 04 02 14](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/929b1225-e59b-4b63-b943-be3989415923)

-------

### De esta manera tenemos activo:
* El entorno virtual con sus librerias
* El server que permite tener activa la base de datos en MariaDB
* El server Flask que nos permite correr la aplicación en localhost

-------

### -> Estructura de la base de datos en MaríaDB (para carga y registro de novedades)

- Tabla "autor": con nombre, apellidos y fecha de nacimiento de cada autor.

  ![Captura de pantalla 2023-06-20 a las 11 09 10](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/5af16113-0ed2-4c89-b3a9-4096a2dc175d)

- Tabla "compra": para seguimiento de los libros vendidos, con información del usuario y la fecha de la operación.

  ![Captura de pantalla 2023-06-20 a las 11 10 23](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/e60f9228-2689-4979-a87c-5fa48b19a54e)

- Tabla "libro": registra el título, el año de edición y el precio de cada libro.

  ![Captura de pantalla 2023-06-20 a las 11 11 29](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/5665a68f-8b18-4fa3-a7cd-acfa830761ac)

- Tabla "tipo_usuario": categorización de cada usuario como Administrador o Cliente.

  ![Captura de pantalla 2023-06-20 a las 11 12 33](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/07203f85-4089-433b-8d06-b5a38c8eab6c)

- Tabla "usuario": lleva el registro de todos los usuarios habilitados con sus correspondientes claves de acceso encriptadas.

  ![Captura de pantalla 2023-06-20 a las 11 14 17](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/9d0b0f50-eed0-4632-9482-91f38d287838)

- Modelo Entidad - Relación

  ![Captura de pantalla 2023-06-20 a las 11 56 03](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/5c1571ac-72f2-429e-93fa-899011dc2ef2)

-------

### -> Funcionalidades de la aplicación en Flask

* Desde Cliente:
 
  * Visualización de libros disponibles y Posibilidad de compra de libros

  ![Captura de pantalla 2023-06-20 a las 12 01 46](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/ef8dc4bd-2f7d-4170-bba2-e5a529cf9b3e)

  * Visualización de mis libros comprados
  
  ![Captura de pantalla 2023-06-20 a las 12 04 03](https://github.com/alebusquet/Flask-Bookstore_Website/assets/110254796/9d0a4088-3354-43cd-8784-b2ca6e2edb42)

* Desde Administrador:
  * Seguimiento de libros vendidos
  * Total de ingresos por cada libro
  * Total de ingresos por el total de libros vendidos

* Logout del sistema


