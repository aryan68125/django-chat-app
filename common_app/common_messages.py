from enum import Enum

class ErrorMessages(Enum):
    #Empty field errors
    EMAIL_FIELD_EMPTY="Email field required!"
    PASSWORD_FIELD_EMPTY = "Password field required!"
    
    #Field validation errors
    EMAIL_NOT_VALID = "Email field is not valid!"