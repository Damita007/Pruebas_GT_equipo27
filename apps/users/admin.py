from django.contrib import admin
from apps.users.models import User

# Register your models here.
admin.site.register(User)     #Permite que en la pagina de /admin, una vez registrado, separe mi app
