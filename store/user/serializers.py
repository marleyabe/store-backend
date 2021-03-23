from rest_framework import serializers
from user.models import User
from django.contrib.auth.models import User as DjangoUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'password', 'username',
                  'first_name', 'last_name', 'email', 'is_active',
                  'phone', 'postalCode', 'typeUser']
