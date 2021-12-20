# InfoBlog
Proyecto para el Informatorio

Usados:
- Python 3.10.X
- Django 3.1
- Windows 10

# Instalacion

  Dependencias: 
  celery=5.1.2
  Django=3.1
  django-crispy-forms=1.12.0
  django-storages=1.11.1
  django-tinymce=3.3.0
  Pillow=8.3.1

  Descargar o clonar y actualizar dependencias.
  
  pip install -r requirements.txt
  
  Actualizacion: En Windows 10 puede haber error al instalar la version de Pillow, hacer la instalacion manual de cada una de las dependencias.
  
  pip install Django==3.1
  pip install celery
  pip install django-crispy-forms
  pip install django-storages
  pip install django-tinymce
  pip install Pillow
  
 # Ejecutar
 
 - Cuenta con base de datos cargada.
- Usuarios:
  * SuperUsuario (contraseña SuperUsuario) Tiene acceso al panel de administacion de Django.
  * UsuarioAdmin (contraseña prueba1234) Perfil Administrador del Blog
  * Claudia (contraseña prueba1234) Perfil Writer
  * Usuario (contrase prueba1234) Perfil normal Reader
  
  python manage.py runserver 127.0.0.1:8000
 
