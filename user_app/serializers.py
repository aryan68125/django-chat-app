from rest_framework import serializers
from user_app.models import UserDetials,User
# import common classes 
from common_app.common_validations import CommonValidations
from rest_framework.serializers import ValidationError

# common error messages
from common_app.common_messages import ErrorMessages,SuccessMessages

# import django password checker 
from django.contrib.auth.hashers import check_password 
class CreateOrUpdateUserProfileSerializer(serializers.ModelSerializer,CommonValidations):
    mobile_number = serializers.CharField(required=False)
    class Meta:
        model = UserDetials
        fields = ["user","name","mobile_number","profile_picture"]

    def validate_mobile_number(self,value):
        result = self.is_phone_no_valid(value)
        if not result.get("status"):
            raise ValidationError(result.get("error"))
        return value 
    
    def create(self,validated_data):
        user = validated_data.pop("user")
        instance,created = UserDetials.objects.update_or_create(
            user = user,
            defaults = validated_data
        )
        return instance
    

class GetUserDetialsSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()
    class Meta:
        model = UserDetials
        fields = ["id","user","name","mobile_number","profile_picture","profile_picture_url","created_at","is_deleted"]

    def get_profile_picture_url(self,obj):
        request = self.context.get("request")
        if obj.profile_picture and hasattr(obj.profile_picture,"url"):
            return request.build_absolute_uri(obj.profile_picture.url)
        return None
    

class ChangePasswordSerializer(serializers.ModelSerializer,CommonValidations):
    old_password = serializers.CharField(write_only = True,required=True,error_messages={"required":ErrorMessages["OLD_PASSWORD_EMPTY"].value})
    password1 = serializers.CharField(write_only = True,required=True,error_messages = {"required":ErrorMessages["PASSWORD_FIELD_EMPTY"].value})
    password2 = serializers.CharField(write_only=True,required=True,error_messages={"required":ErrorMessages["PASSWORD_FIELD_EMPTY"].value})
    class Meta:
        model = User
        fields = ["old_password", "password1", "password2", "is_active", "is_deleted"] 

    def validate_old_password(self,value):
        result = self.is_password_valid(value)
        if not result.get("status"):
            raise ValidationError(result.get("error"))
        return value
    
    def validate_password1(self,value):
        result = self.is_password_valid(value)
        if not result.get("status"):
            raise ValidationError(result.get("error"))
        return value
    
    def validate_password2(self,value):
        result = self.is_password_valid(value)
        if not result.get("status"):
            raise ValidationError(result.get("error"))
        return value
    
    def create(self,validated_data):
        request = self.context.get("request")
        old_password = validated_data.pop("old_password")
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        if not password1 == password2:
            raise ValidationError(ErrorMessages["PASSWORD_NOT_MATCHING"].value)
        logged_in_user_id = request.user.id
        # check if the logged in user exists
        user_instance = User.objects.filter(id=logged_in_user_id,is_deleted=False).first()
        if not user_instance:
            raise ValidationError(ErrorMessages["LOGGEDIN_USER_NOT_FOUND"].value)
        # check if the old password is correct
        if not check_password(old_password,user_instance.password):
            raise ValidationError(ErrorMessages["PASSWORD_INCORRECT"].value)
        # now change the password 
        user_instance.set_password(password1)
        user_instance.save()
        return user_instance
        

