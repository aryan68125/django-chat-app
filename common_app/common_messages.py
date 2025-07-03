from enum import Enum

class ErrorMessages(Enum):
    #Empty field errors
    EMAIL_FIELD_EMPTY = "Email field required!"
    OLD_PASSWORD_EMPTY = "Old password required!"
    PASSWORD_FIELD_EMPTY = "Password field required!"    
    #Field validation errors
    EMAIL_NOT_VALID = "Email field is not valid!"
    PASSWORD_NOT_VALID = "Password field is not valid! Password must contain at least 8 characters, including uppercase, lowercase, numbers, and special characters."
    PASSWORD_NOT_MATCHING = "Passwords in the new password and confirm password fields are not matching"
    # PHONE NUMBER ERROR
    PHONE_NUMBER_LENGTH_ERROR = "Phone number must be 10 digits long"
    PHONE_NUMBER_IS_NOT_A_NUMBER = "Phone number must be a number"

    # Login errors
    INVALID_CREDENTIALS = "Invalid credentials! Please check your email and password."
    ACCOUNT_NOT_FOUND = "Account not found! Please register first or check your email."
    PASSWORD_INCORRECT = "Password is incorrect! Please try again."

    # INTERNAL SERVER ERROR
    SOMETHING_WENT_WRONG = "Something went wrong! Please try again later."

    # USER PROFILE DATA NOT FOUND
    USER_PROFILE_DATA_NOT_FOUND = "User profile data not found"
    LOGGEDIN_USER_NOT_FOUND = "Logged in user not found"


class SuccessMessages(Enum):
    ACCOUNT_REGISTERED = "Account registered successfully!"
    LOGIN_SUCCESS = "Welcome!"

    USER_PROFILE_UPDATED = "Your profile has been updated"
    USER_PASSWORD_UPDATED = "You password is changes successfully!"

    USER_LOGOUT_SUCCESS = "Good bye see you soon!"
    