from rest_framework.views import APIView
from common_app.common_messages import ErrorMessages,SuccessMessages
from common_app.views_bl import CommonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework import status
# import serializers
from user_app.serializers import CreateOrUpdateUserProfileSerializer,GetUserDetialsSerializer,ChangePasswordSerializer
# model import 
from user_app.models import UserDetials
from rest_framework.serializers import ValidationError
"""Users profile page related APIS STARTS"""
class ProcessUserProfileData(APIView,CommonResponse):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser,FormParser]
    """
    This api is used to insert new data in the User's profile table or update the existing data in that table
    """
    def post(self,request):
        try:
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
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value,message=e)

    """This api is used to get the User's profile data"""
    def get(self,request):
        try:
            logged_in_user_id = request.user.id
            user_detials_instance = UserDetials.objects.filter(user=logged_in_user_id,is_deleted=False).first()
            if not user_detials_instance:
                return self.common_web_response(status_code=status.HTTP_404_NOT_FOUND,error=ErrorMessages["USER_PROFILE_DATA_NOT_FOUND"].value)
            serializer = GetUserDetialsSerializer(user_detials_instance, context={"request": request})
            return self.common_web_response(status_code=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value,message=e)
        

class ProcessChangePassword(APIView,CommonResponse):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    parser_classes = [JSONParser, FormParser]
    def put(self,request):
        try:
            serializer = ChangePasswordSerializer(data=request.data,context={"request":request})
            print(f"serializer :: {serializer}")
            if not serializer.is_valid():
                print("Serializer is invalid:", serializer.errors)
                return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=serializer.errors)
            serializer.save()
            return self.common_web_response(status_code=status.HTTP_200_OK,message=SuccessMessages["USER_PASSWORD_UPDATED"].value)
        except ValidationError as ve:
            return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=ve.detail)
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value,message=e)
"""Users profile page related APIS ENDS"""