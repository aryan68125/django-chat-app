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
class RegisterUser(serializers.ModelSerializer,CommonValidations):
    email = serializers.EmailField(required=True,error_message = {"required":ErrorMessages['EMAIL_FIELD_EMPTY'].value})
    password = serializers.CharField(required=True,error_message = {"required":ErrorMessages['PASSWORD_FIELD_EMPTY'].value})
    class Meta:
        model = User
        fields = ['email','password']

    """validate email pattern and uniqueness"""
    def validate_email(self,value):
        if not self.is_email_valid(value):
            raise serializers.ValidationError(ErrorMessages['EMAIL_NOT_VALID'].value)
        start from here ===> 
        ===> add is_deleted field in the User model
        ===> add a logic to make sure that the user is notified if the email is taken by another user which has is_deleted flag set to False only 
        ===> If a user has the email address which is present in another user reacord which is deleted then that record must be updated in the User table during the registration process and must be allowed to create the account. 
        if User.objects.filter(email=value.lower())