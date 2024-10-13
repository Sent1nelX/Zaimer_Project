from rest_framework import serializers
from .models import (Client, Passport, PotentialClient, TelegramUser, TelegramUserLog)

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'

class TelegramUserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserLog
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    passports = serializers.StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = '__all__'

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = '__all__'

class PotentialClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialClient
        fields = '__all__'
