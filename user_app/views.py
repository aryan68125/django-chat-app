from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication , permissions
from rest_framework import status
# Create your views here.
class test(APIView):
    # authentication_classes = (authentication.SessionAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self,request):
        test_data = request.data.get('test_data')
        print(f"test_data recieved : {test_data}")
        data = {
            "test_data":test_data
        }
        return Response({'status_code':status.HTTP_200_OK,'message':'test_data recieved','data':data})