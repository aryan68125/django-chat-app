from rest_framework.response import Response

# This class is used in every web api end-points to send an api response that is uniform accross the entire application
class CommonResponse:
    def common_web_response(self,status_code=None,error=None,message=None,data=None):
        if not status_code:
            return {'error':'status_code required'}
        if not error:
            error = ""
        if not message:
            message = ""
        if not data:
            data = {}
        return Response({'status_code':status_code,'error':error,'message':message,'data':data})