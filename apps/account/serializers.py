from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        write_only=True  # post only
    )
    token = serializers.CharField(
        read_only=True  # get only
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', "password", "password_confirm")

    def validate(self, attrs):  # вызывается во время is_valid
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")

        if len(password) < 8 or len(password_confirm) < 8:
            raise serializers.ValidationError('password or password_confirm <8 characters')

        if password != password_confirm:
            raise serializers.ValidationError("password or password_confirm not equal!!!")

        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)