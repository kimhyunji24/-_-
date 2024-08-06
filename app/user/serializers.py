"""
Serializers for the user API View
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password':{'write_only':True, 'min_length':4}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = get_user_model().objects.filter(email=value).first()
        if not user:
            raise serializers.ValidationError('No user is associated with this email address.')
        return value

    def save(self):
        request = self.context.get('request')
        email = self.validated_data['email']
        user = get_user_model().objects.get(email=email)

        token = default_token_generator.make_token(user)

        reset_link = f"{settings.FRONTEND_URL}/reset-password?token={token}&email={email}"
        send_mail(
            'Password Reset',
            f'Click the link to reset your password: {reset_link}',
            'no-reply@example.com',
            [email],
            fail_silently=False,
        )

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        token = attrs.get('token')
        user = get_user_model().objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError('Invalid email address.')

        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError('Invalid token.')

        return attrs
    
    def save(self):
        email = self.validated_data['email']
        new_password = self.validated_data['new_password']
        user = get_user_model().objects.get(email=email)
        user.set_password(new_password)
        user.save()
"""
class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return data
"""