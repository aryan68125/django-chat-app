from rest_framework.views import APIView
from common_app.common_messages import ErrorMessages,SuccessMessages
from common_app.views_bl import CommonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
# import serializers
from user_app.serializers import CreateOrUpdateUserProfileSerializer
class ProcessUserProfileData(APIView,CommonResponse):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser,FormParser]
    """
    This api is used to insert new data in the User's profile table or update the existing data in that table
    """
    def post(self,request):
        user = request.user
        name = request.data.get("name")
        mobile_number = request.data.get("phonenumber")
        profile_picture = request.FILES.get("profile_photo")
        data = {
            "user":user.id,
            "name":name,
            "mobile_number":mobile_number,
            "profile_picture":profile_picture,
        }
        serializers = CreateOrUpdateUserProfileSerializer(data=data)
        if not serializers.is_valid():
            return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=serializers.errors)
        serializers.save()
        return self.common_web_response(status_code=status.HTTP_200_OK,message=SuccessMessages["USER_PROFILE_UPDATED"].value)

    """This api is used to get the User's profile data"""
    def get(self,request):
        pass