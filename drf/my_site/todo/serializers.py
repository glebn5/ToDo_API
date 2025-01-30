from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User

# Сериалайзер для регистрации
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validate_data):
        user = User(
            username = validate_data['username'],
            email = validate_data['email'],
            
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

# Сериайлайзер для данных из бд
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
