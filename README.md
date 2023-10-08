# API REST USUARIOS V1.0.0

## Comenzando 🚀   
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_Requerimientos mínimos del sistema._


1. Python3.x.
2. virtualenv.

### Instalación 🔧

_Sigue los siguientes pasos despues de tener instalado todos los requisitos mensionados enteriormente._

Descarga el proyecto desde el repositorio, desde la consola ejecuta el siguiente comando dentro de un directorio de tu elección.
```
$ git clone https://github.com/JoseMMenchaca/django.git
```
Desde la consola de comando ingresa hasta el directorio del proyecto descargado ejecutando el siguiente comando.
```
$ cd /api-usuarios

```

Dentro del directorio del proyecto ejecuta los siguientes comandos para crear un entorno virtual y activarlo.

```
$ python -m venv .venv
$ .\.venv\Scripts\activate
```
Despues de activar el entorno virtual, ejecuta el siguiente comando para instalar las librerias requeridas para el funcionamiento del sistema.

```
(env)$ pip install -r requirements.txt
```

Ejecutar las siguientes lineas en la consola para generar las migraciones y tablas de la base de datos
````
python manage.py makemigrations
python manage.py migrate
````

Finalmente tienes listo el Api Rest para su funcionamiento y consumo, para poner en marcha el servidor de desarrollo ejecuta el siguiente comando.
````
(env)$ python manage.py runserver
````


## Autores ✒️

* [CARLOS ALBERTO MENCHACA ENCINAS] *
* [JOSÉ MANUEL MENCHACA ENCINAS] *