from common_app.common_regex_pattern import CommonValidationPatterns
import re
class CommonValidations:
    def is_email_valid(self,email):
        if re.match(CommonValidationPatterns['EMAIL'].value, email):
            return {'status':True,'message':'Email is valid!'}
        else:
            return {'status':False,'error':'Email not valid!'}