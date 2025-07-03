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
# email related imports
from auth_app.tasks import send_email_task
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.urls import reverse
from django.db import transaction
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
        with transaction.atomic():
            try:
                """
                Check if the user is already in database with is_deleted = False
                """
                existing_user = User.objects.filter(email=validated_data.get("email").lower(),is_deleted=True).first()
                if existing_user:
                    """Update the existing user if found"""
                    existing_user.is_active = False
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
                        is_active=False,
                        is_admin=False,
                        is_deleted=False,
                    )
                # Prepare email
                current_year = timezone.now().year
                uid = urlsafe_base64_encode(force_bytes(user_instance.pk))
                token = default_token_generator.make_token(user_instance)
                request = self.context.get("request")
                relative_path = reverse("verify_account_page", kwargs={"uid": uid, "token": token})
                url = request.build_absolute_uri(relative_path) 
                verification_link = url
                print(f"verification_link ==> {verification_link}")
                html_message = render_to_string("email_templates/register_verify_email.html",{
                    "verification_link":verification_link,
                    "current_year":current_year
                })
                send_email_task.delay(
                    subject = "Verify your account to activate your account",
                    EMAIL_HOST_USER = settings.EMAIL_HOST_USER,
                    recipient_list = [user_instance.email],
                    html_message=html_message,
                )
                return user_instance
            except Exception as e:
                return serializers.ValidationError(f"User registration failed {str(e)}")
        

class ActivateAccountSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True,error_messages = {"required":ErrorMessages["UID_SERIALIZER_ERROR"].value})
    token = serializers.CharField(required=True,error_messages = {"required":ErrorMessages["TOKEN_SERIALIZER_ERROR"].value})
    class Meta:
        model = User
        fields = ["is_active","uid","token"]

    def create(self,validated_data):
        uid = validated_data.pop("uid")
        token = validated_data.pop("token")
        uid_decoded = force_str(urlsafe_base64_decode(uid))
        user = User.objects.filter(is_deleted=False,pk=uid_decoded).first()
        if not user:
            raise ValidationError(ErrorMessages["ACCOUNT_NOT_FOUND"].value)
        if not default_token_generator.check_token(user,token):
            raise ValidationError(ErrorMessages["INVALID_TOKEN"].value)
        user.is_active = True
        user.save()
        return user


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

        