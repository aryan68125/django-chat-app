from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout

# import response utility
from common_app.views_bl import CommonResponse

# celery related imports
from auth_app.tasks import send_email_task
from celery.result import AsyncResult
from django_celery_results.models import TaskResult

#email related imports
from django.template.loader import render_to_string
from django.conf import settings

from auth_app.serializers import RegisterUserSerializer,LoginUserSerializer, ActivateAccountSerializer
from rest_framework.exceptions import ValidationError
from common_app.common_messages import ErrorMessages,SuccessMessages

class RegisterUser(APIView, CommonResponse):
    """this api end point is used to verify email and activate the account after the user account is created"""
    def put(self,request):
        try:
            uid = request.data.get("uid")
            token = request.data.get("token")
            data={
                "uid":uid,
                "token":token
            }
            serializer = ActivateAccountSerializer(data=data)
            if not serializer.is_valid():
                return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=serializer.errors)
        
            serializer.save()
            return self.common_web_response(status_code=status.HTTP_200_OK,message=SuccessMessages["ACCOUNT_ACTIVATED"].value)
        except ValidationError as ve:
            return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=ve.detail)
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value,message=e)
        
        
    """this api end point creates an account for the user during the registration process"""
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            front_end_data = {
                "email":email,
                "password":password
            }
            serializer = RegisterUserSerializer(data= front_end_data,context={"request":request})
            if not serializer.is_valid():
                return self.common_web_response(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    error=serializer.errors
                )
            serializer.save()
            return self.common_web_response(
                status_code=status.HTTP_201_CREATED,message=SuccessMessages["ACCOUNT_REGISTERED"].value
            )
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value,message=e)


class LoginUser(APIView,CommonResponse):
    def post(self,request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            data = {
                "email":email,
                "password":password
            }
            login_serializer = LoginUserSerializer(data=data,context={"request":request})
            if not login_serializer.is_valid():
                return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=login_serializer.errors)
            # sice I wrote my login code inside the create function I have to trigger it manually using this seiralizer.save() method
            login_serializer.save() 
            return self.common_web_response(status_code=status.HTTP_200_OK,message=SuccessMessages["LOGIN_SUCCESS"].value)
        except ValidationError as ve:
            return self.common_web_response(status_code=status.HTTP_400_BAD_REQUEST,error=ve.detail)
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value, message=e)
        

class LogoutUser(APIView,CommonResponse):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [SessionAuthentication,]
    def post(self,request):
        try:
            logout(request)
            return self.common_web_response(status_code=status.HTTP_200_OK,message=SuccessMessages["USER_LOGOUT_SUCCESS"].value)
        except Exception as e:
            return self.common_web_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,error=ErrorMessages["SOMETHING_WENT_WRONG"].value,message=e)