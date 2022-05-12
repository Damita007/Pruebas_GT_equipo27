# #ARCHIVO PRUEBA 2 Modificaciones usando managers.py, de página: https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
#from attr import fields
from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager   #este hay que agregar


class CustomUser(AbstractUser):  #Creo nueva clase llamada CustomerUser y subclase AbstractUser
    username = None     #Se elimina campo de username
    email = models.EmailField(_('Correo electrónico'), max_length=40, unique=True)   #Email campo obligatorio y unico
    status = models.BooleanField(null=True)
    historical = HistoricalRecords()
    objects = CustomUserManager()   #Se especifica que todos los objetos de la clase provienen de CustomerUserManager

    USERNAME_FIELD = 'email'   #Define al email como el identificador unico para el modelo User 
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

   

    












# #ARCHIVO PRUEBA 2 Funciona con las modificaciones hechas
# import email
# from django.db import models
# from django.contrib.auth.models import AbstractUser #, PermissionsMixin
# # from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import BaseUserManager #, AbstractBaseUser
# from simple_history.models import HistoricalRecords
# # se quita AbstractBaseUser y de deja AbstractUser


# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, is_applicant, is_employer, **extra_fields):  #name, last_name,  #username
#         user = self.model(
#             email = email,
#             is_staff = is_applicant,
#             is_superuser = is_employer,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):  
#         return self._create_user(email, password, False, False, **extra_fields) 

#     def create_superuser(self, email, password=None, **extra_fields):
#         return self._create_user(email, password, True, True, **extra_fields) 


# is_applicant = models.BooleanField('status_solicitante', default = False)
# is_employer = models.BooleanField('status_empleador', default = False)


# class User(AbstractUser):#PermissionsMixin
#     name = models.CharField('Nombres', max_length = 255, null = True)   #unique = True, unique=True para que sea un campo requerido y obligatorio
#     last_name = models.CharField('Apellidos', max_length = 255, null = True)    #blank = True,
#     email = models.EmailField('Correo Electrónico', max_length = 50, unique = True, null = True)
#     gender = models.CharField(verbose_name='Genero', max_length = 50, null = True)   #blank = True,
#     birth_date = models.DateField(verbose_name='Fecha de nacimiento', null = True) 
#     marital_status = models.CharField(verbose_name='Estado civil', max_length = 50, null = True)
#     age = models.IntegerField(verbose_name='Edad', null=True)
#     email_alternative = models.EmailField('Correo Electrónico alternativo',max_length = 255, null = True)
#     residence = models.CharField('Residencia actual', max_length = 255, null = True) #blank = True,
#     image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True)  #blank = True,
#     is_applicant = models.BooleanField('status_solicitante', default = False)
#     is_employer = models.BooleanField('status_empleador', default = False)
#     historical = HistoricalRecords()
#     objects = UserManager()
   
#     class Meta:
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


#     def __str__(self):
#         return f'{self.name} {self.last_name}'

        













# #ARCHIVO PRUEBA1 FUNCIONANDO OK
# from django.db import models
# #from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from simple_history.models import HistoricalRecords
# #from django.utils import timezone   #Para saber el tiempo exacto en DateTimeField(default=timezone.now)


# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):  #name, last_name,  #username
#         user = self.model(
#             #username = username,
#             email = email,
#             # name = name,
#             # last_name = last_name,
#             is_staff = is_staff,
#             is_superuser = is_superuser,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):  #name, last_name,    #username
#         return self._create_user(email, password, False, False, **extra_fields) #name,last_name,   #username

#     def create_superuser(self, email, password=None, **extra_fields): #name,last_name,    #username
#         return self._create_user(email, password, True, True, **extra_fields) #name,last_name,   #username

# class User(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField('Nombres', max_length = 255, null = True)   #unique = True, unique=True para que sea un campo requerido y obligatorio
#     email = models.EmailField('Correo Electrónico', max_length = 50, unique = True, null = True) 
#     last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
#     gender = models.CharField(verbose_name='Genero', max_length = 50, blank = True, null = True)
#     birth_date = models.DateField(verbose_name='Fecha de nacimiento', null = True) 
#     marital_status = models.CharField(verbose_name='Estado civil', max_length = 50, null = True)
#     age = models.IntegerField(verbose_name='Edad', null=True)
#     email_alternative = models.EmailField('Correo Electrónico alternativo',max_length = 255, null = True)
#     residence = models.CharField('Residencia actual', max_length = 255, blank = True, null = True)
#     image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
#     is_active = models.BooleanField(default = True)
#     is_staff = models.BooleanField(default = False)
#     historical = HistoricalRecords()
#     objects = UserManager()

#     class Meta:
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

    
#     #EMAIL_FIELD = 'email'                            #USERNAME_FIELD = 'username'
#     #REQUIRED_FIELDS = ['email_alternative', 'last_name']   #REQUIRED_FIELDS = ['email','name','last_name']  #GT debe contener todos los campos obligatorios de mi modelo users, pero no debe tener USERNAME_FIELD or PASSWORD_FIELD, ya que esos siempre se solicitaran

#     def __str__(self):
#         return f'{self.name} {self.last_name}'

        


# #ARCHIVO ORIGINAL PARA HACER PRUEBAS

# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from simple_history.models import HistoricalRecords


# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
#         user = self.model(
#             username = username,
#             email = email,
#             name = name,
#             last_name = last_name,
#             is_staff = is_staff,
#             is_superuser = is_superuser,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_user(self, username, email, name,last_name, password=None, **extra_fields):
#         return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

#     def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
#         return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length = 255, unique = True)
#     email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
#     name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
#     last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
#     image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
#     is_active = models.BooleanField(default = True)
#     is_staff = models.BooleanField(default = False)
#     historical = HistoricalRecords()
#     objects = UserManager()

#     class Meta:
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email','name','last_name']

#     def __str__(self):
#         return f'{self.name} {self.last_name}'

