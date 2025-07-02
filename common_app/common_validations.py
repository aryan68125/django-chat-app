from common_app.common_regex_pattern import CommonValidationPatterns
import re
from common_app.common_messages import ErrorMessages
class CommonValidations:
    def is_email_valid(self,email):
        if re.match(CommonValidationPatterns['EMAIL'].value, email):
            return {'status':True,'message':'Email is valid!'}
        else:
            return {'status':False,'error':ErrorMessages["EMAIL_NOT_VALID"].value}
    def is_password_valid(self,password):
        if re.match(CommonValidationPatterns["PASSWORD"].value,password):
            return {"status":True,"message":"Password is valid!"}
        else:
            return {"status":False,"error":ErrorMessages["PASSWORD_NOT_VALID"].value}
        
    def is_phone_no_valid(self,phone_number):
        if not len(phone_number) == 10:
            return {"status":False,"error":ErrorMessages["PHONE_NUMBER_LENGTH_ERROR"].value}
        if not phone_number.isdigit():
            return {"status":False,"error":ErrorMessages["PHONE_NUMBER_IS_NOT_A_NUMBER"].value}
        return {"status":True}
        