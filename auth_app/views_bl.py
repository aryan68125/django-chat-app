from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status


# import response utility
from common_app.views_bl import CommonResponse

# just for testing purposes 
from auth_app.tasks import add
from celery.result import AsyncResult

class RegisterUser(APIView, CommonResponse):
    # Create new users in the database during the registration process
    def post(self,request):
        x = request.data.get('x')
        y = request.data.get('y')
        result = add.delay(x,y)
        data = {
            "task_id": result.id,
            "status": result.status,
            "result": result.result if result.ready() else None
        }
        return self.common_web_response(status_code=status.HTTP_201_CREATED,message="Your account has been created successfully!",data=data)
