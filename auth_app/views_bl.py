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

class RegisterUser(APIView, CommonResponse):
    def post(self, request):
        return self.common_web_response(
            status_code=status.HTTP_201_CREATED,
        )

