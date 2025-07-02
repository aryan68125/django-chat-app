from rest_framework import serializers
from user_app.models import UserDetials,User
# import common classes 
from common_app.common_validations import CommonValidations
from rest_framework.serializers import ValidationError

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
    
