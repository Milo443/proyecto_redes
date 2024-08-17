FTP-Cliente Django

Descripción

Este proyecto es un cliente FTP en Django que se conecta a un servidor FTP en Linux. Permite a los usuarios descargar y subir archivos a un servidor FTP remoto después de iniciar sesión con su cuenta.

Requisitos

- Django 3.2 o superior
- Python 3.8 o superior
- Servidor FTP en Linux (por ejemplo, vsftpd)

Configuración

1. Instalar las dependencias: pip install -r requirements.txt
2. Configurar la conexión FTP en (link unavailable):

FTP_HOST = '(link unavailable)'
FTP_USER = 'usuario'
FTP_PASSWORD = 'contraseña'
FTP_PORT = 21

1. Crear un usuario y contraseña en el servidor FTP
2. Ejecutar el proyecto: python (link unavailable) runserver

Funcionalidades

- Inicio de sesión con cuenta de usuario
- Conexión a un servidor FTP remoto
- Descarga de archivos desde el servidor FTP
- Subida de archivos al servidor FTP
- Mostrar lista de archivos en el servidor FTP

Uso

1. Acceder a la interfaz web del cliente FTP: http://localhost:8000/ftp
2. Iniciar sesión con su cuenta de usuario
3. Introducir la dirección del servidor FTP, usuario y contraseña
4. Seleccionar el archivo que se desea descargar o subir
5. Presionar el botón "Descargar" o "Subir" para realizar la acción
