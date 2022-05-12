#Convierte cualquier estructura del modelo User a formato JSON para consulta
from rest_framework import serializers
from apps.users.managers import CustomUserManager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserManager
        fields = '__all__'


from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = '__all__'