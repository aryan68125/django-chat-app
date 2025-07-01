from rest_framework.views import APIView
from common_app.common_messages import ErrorMessages,SuccessMessages
from common_app.views_bl import CommonResponse

class ProcessUserProfileData(APIView,CommonResponse):
    """This api is used to insert new data in the User's profile data"""
    def post(self,request):
        pass
    """This api is used to update the User's profile data"""
    def patch(self,request):
        pass
    """This api is used to get the User's profile data"""
    def get(self,request):
        pass