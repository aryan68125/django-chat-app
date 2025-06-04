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
        subject = "This is a test email sent by django-chat-app"
        message = "Hello, This is a test email sent by django-chat-app"
        if not subject:
            return self.common_web_response(status_code=status.HTTP_404_NOT_FOUND,error="Email subject not found!")
        if not message:
            return self.common_web_response(status_code=status.HTTP_404_NOT_FOUND,error="Email message body not found!")
        html_message = render_to_string('email_templates/register_verify_email.html',{
            "user_name":"Aditya Kumar test user from views"
        })
        recipient_list = ["aryan68125@gmail.com"]
        send_email_task.delay(subject,message,settings.EMAIL_HOST_USER,recipient_list,html_message)
        return self.common_web_response(
            status_code=status.HTTP_201_CREATED,
            message="Email sent successfully.",
        )

