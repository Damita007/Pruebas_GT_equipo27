"""
La documentación oficial de Django recomienda encarecidamente utilizar 
un modelo de usuario personalizado. Esto proporciona mucha más flexibilidad 
en el futuro, por lo que, como regla general, siempre use un modelo de 
usuario personalizado para todos los proyectos nuevos de Django .
"""
"""
Modelo de usuario: CustomerUserManager 
Subclase: BaseUserManager
indicarle que use un correo electrónico como identificador único
en lugar de un nombre de usuario.
"""
# https://testdriven.io/blog/django-custom-user-model/

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Debe colocarse dirección de Email'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))     
        return self.create_user(email, password, **extra_fields)

