from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status

# import response utility
from common_app.views_bl import CommonResponse
class RegisterUser(APIView, CommonResponse):
    # Create new users in the database during the registration process
    def post(self,request):
        email_id = request.data.get('email_id')
        password = request.data.get('password')
        print(f"email_id = {email_id} :: password = {password}")
        data = {
            'email_id':email_id,
            'password':password
        }
        return self.common_web_response(status_code=status.HTTP_201_CREATED,message="Your account has been created successfully!",data=data)
