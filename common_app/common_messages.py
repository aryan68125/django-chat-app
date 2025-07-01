from enum import Enum

class ErrorMessages(Enum):
    #Empty field errors
    EMAIL_FIELD_EMPTY="Email field required!"
    PASSWORD_FIELD_EMPTY = "Password field required!"
    
    #Field validation errors
    EMAIL_NOT_VALID = "Email field is not valid!"
    PASSWORD_NOT_VALID = "Password field is not valid! Password must contain at least 8 characters, including uppercase, lowercase, numbers, and special characters."

    # Login errors
    INVALID_CREDENTIALS = "Invalid credentials! Please check your email and password."
    ACCOUNT_NOT_FOUND = "Account not found! Please register first or check your email."
    PASSWORD_INCORRECT = "Password is incorrect! Please try again."

    # INTERNAL SERVER ERROR
    SOMETHING_WENT_WRONG = "Something went wrong! Please try again later."

class SuccessMessages(Enum):
    ACCOUNT_REGISTERED = "Account registered successfully!"
    LOGIN_SUCCESS = "Login Successful!"
    