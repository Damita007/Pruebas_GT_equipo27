from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    ordering = ('email',)   #Para evitar error (admin.E031)
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )    

search_fields = ('email',)
ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin) 
















# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser


# # Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     ordering = ('email',)   #Para evitar error (admin.E031)
#     list_display = ["email", "password",]
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields':('custom_field',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields':('custom_field',)}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin) #, CustomUserAdmin   #Permite que en la pagina de /admin, una vez registrado, separe mi app
