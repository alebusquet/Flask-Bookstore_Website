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

1.	Creación del entorno de trabajo
    
    Clonar el repositorio
    
    Creación del entorno virtual: `python3 -m venv venv-Flask`
    
    Activación del entorno: `source venv-Flask/bin/activate`
    
    Instalación de librerías mediante el archivo requirements.txt: `pip install -r requirements.txt`
    
    Una vez contamos con estos pasos previos, se activa el server de Flask para poder acceder a la aplicación mediante el “localhost”: `python manage.py runserver`.
    
    En el navegador, en la dirección http://127.0.0.1:5000/login se puede acceder a la aplicación, como puede verse abajo (imagen)

