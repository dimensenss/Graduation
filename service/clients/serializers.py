from django.contrib.auth.hashers import make_password
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


# class ClientCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         fields = ('id', 'email', 'password')

