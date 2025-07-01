from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status


# import response utility
from common_app.views_bl import CommonResponse

# celery related imports
from auth_app.tasks import send_email_task
from celery.result import AsyncResult
from django_celery_results.models import TaskResult

#email related imports
from django.template.loader import render_to_string
from django.conf import settings

from auth_app.serializers import RegisterUserSerializer,LoginUserSerializer
from common_app.common_messages import ErrorMessages,SuccessMessages
class RegisterUser(APIView, CommonResponse):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        front_end_data = {
            "email":email,
            "password":password
        }
        serializer = RegisterUserSerializer(data= front_end_data)
        if not serializer.is_valid():
            return self.common_web_response(
                status_code=status.HTTP_400_BAD_REQUEST,
                error=serializer.errors
            )
        serializer.save()
        return self.common_web_response(
            status_code=status.HTTP_201_CREATED,message=SuccessMessages["ACCOUNT_REGISTERED"].value
        )

class LoginUser(APIView,CommonResponse):
    def post(self,request):
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