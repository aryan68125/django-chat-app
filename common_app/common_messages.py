from enum import Enum

class ErrorMessages(Enum):
    #Empty field errors
    EMAIL_FIELD_EMPTY="Email field required!"
    PASSWORD_FIELD_EMPTY = "Password field required!"
    
    #Field validation errors
    EMAIL_NOT_VALID = "Email field is not valid!"
    PASSWORD_NOT_VALID = "Password field is not valid! Password must contain at least 8 characters, including uppercase, lowercase, numbers, and special characters."

class SuccessMessages(Enum):
    ACCOUNT_REGISTERED = "Account registered successfully!"
    LOGIN_SUCCESS = "Login Successful!"
    