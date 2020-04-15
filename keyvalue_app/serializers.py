from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()

from . import models

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class KeyValuePairSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KeyValuePair
        fields = "__all__"

class KeyFilePairSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KeyFilePair
        fields = "__all__"