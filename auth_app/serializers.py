#django serializer realted imports
from rest_framework import serializers
#django db realted imports
from django.db import transaction
#model related imports
from user_app.models import User
#common error messages related errors
from common_app.common_messages import ErrorMessages
#common validation class realted imports
from common_app.common_validations import CommonValidations
from rest_framework import serializers
from user_app.models import User
from rest_framework.serializers import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password

class RegisterUserSerializer(serializers.ModelSerializer,CommonValidations):
    email = serializers.EmailField(required=True, max_length=70,error_messages ={"required":ErrorMessages["EMAIL_FIELD_EMPTY"].value})
    password = serializers.CharField(write_only = True,required=True,error_messages = {"required":ErrorMessages["PASSWORD_FIELD_EMPTY"].value})
    class Meta:
        model = User
        fields = ["email","password","is_active","is_admin","is_deleted"]
        
    def validate_email(self,value):
        """Validate the email field"""
        if not self.is_email_valid(value).get("status"):
            raise serializers.ValidationError(self.is_email_valid(value).get("error"))
        return value
    
    def validate_password(self,value):
        """Validate the password field"""
        if not self.is_password_valid(value).get("status"):
            raise serializers.ValidationError(self.is_password_valid(value).get("error"))
        return value
    
    def create(self,validated_data):
        """
        Check if the user is already in database with is_deleted = False
        """
        existing_user = User.objects.filter(email=validated_data.get("email").lower(),is_deleted=True).first()
        if existing_user:
            """Update the existing user if found"""
            existing_user.is_active = True
            existing_user.is_deleted = False
            existing_user.email = validated_data.get("email").lower()
            existing_user.password = make_password(validated_data.get("password"))
            existing_user.save()
            user_instance = existing_user
        else:
            """
            Create a new user with the validated_data here

            Ideally is_active=True, must be False for new users but since I am not verifying emails hence I am keeping it True so the user can login immediately.
            """
            user_instance = User.objects.create(
                email=validated_data.get("email").lower(),
                password=make_password(validated_data.get("password")),
                is_active=True,
                is_admin=False,
                is_deleted=False,
            )
        return user_instance
        

class LoginUserSerializer(serializers.Serializer,CommonValidations):
    email = serializers.EmailField(required=True,max_length=100,error_messages = {"required":ErrorMessages["EMAIL_FIELD_EMPTY"].value})
    password = serializers.CharField(write_only=True,required=True,error_messages = {"required":ErrorMessages["PASSWORD_FIELD_EMPTY"].value})

    def validate_email(self,value):
        """Validate email field"""
        if not self.is_email_valid(value).get("status"):
            raise serializers.ValidationError(self.is_email_valid(value).get("error"))
        return value
    
    def validate_password(self,value):
        """Validate passowrd field"""
        if not self.is_password_valid(value).get("status"):
            raise serializers.ValidationError(self.is_password_valid(value).get("error"))
        return value
    
    def create(self,validated_data):
        email = validated_data.get("email").lower()
        password = validated_data.get("password")
        user_instance = User.objects.filter(email=email,is_deleted=False).first()
        if not user_instance:
            raise ValidationError(ErrorMessages["ACCOUNT_NOT_FOUND"].value)
        
        if not check_password(password,user_instance.password):
            raise ValidationError(ErrorMessages["PASSWORD_INCORRECT"].value)
        login(self.context.get("request"),user_instance)
        return user_instance

        