from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status


# import response utility
from common_app.views_bl import CommonResponse

# just for testing purposes 
from auth_app.tasks import add
from celery.result import AsyncResult
from django_celery_results.models import TaskResult

class RegisterUser(APIView, CommonResponse):
    def post(self, request):
        x = int(request.data.get('x', 0))
        y = int(request.data.get('y', 0))
        result = add.delay(x, y)
        task_result = AsyncResult(result.id)

        data = {
            "task_id": result.id,
            "status": task_result.status,
            "result": task_result.result if task_result.ready() else None,
        }
        return self.common_web_response(
            status_code=status.HTTP_201_CREATED,
            message="Task submitted successfully.",
            data=data
        )

