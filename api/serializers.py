from rest_framework import serializers
from .models import Report, Actor, Company
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
                               get_username_max_length)

from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=20, min_length=5)
#     password = serializers.CharField(max_length=65, min_length=6, write_only=True)
#     email = serializers.EmailField(max_length=255, min_length=6),
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'email', ('Email is already in use.')})
#         return super().validate(attrs)
#
#     def create(self, **validated_data):
#         return User.objects.create_user(**validated_data)
#
# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         max_length=get_username_max_length(),
#         min_length=allauth_settings.USERNAME_MIN_LENGTH,
#         required=allauth_settings.USERNAME_REQUIRED
#     )
#     email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#
#     def validate_username(self, username):
#         username = get_adapter().clean_username(username)
#         return username
#
#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."))
#         return email
#
#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)
#
#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(_("The two password fields didn't match."))
#         return data
#
#     def custom_signup(self, request, user):
#         pass
#
#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', '')
#         }
#
#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         return user
#
#
# class RegistrationSerializer(serializers.ModelSerializer):
#
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password', 'password2')
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def save(self):
#         user = User.objects.create_user(
#                 email=self.validated_data['email'],
#                 username=self.validated_data['username']
#             )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         user.set_password(password)
#         user.save()
#         return user



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'title', 'content', 'city', 'state', 'actor', 'actor_name', 'company_name', 'company', 'created_date',
                  'updated_date', 'user')


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'fName', 'lName', 'job_position')


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'industry')
