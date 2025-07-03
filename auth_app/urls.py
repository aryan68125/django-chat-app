from django.urls import path

from auth_app.views_bl import RegisterUser,LoginUser,LogoutUser
from auth_app.views import register_user_page,login_user_page
urlpatterns = [
    # business logic realted routes
    path('resgister-user-bl/',RegisterUser.as_view(),name="RegisterUser"),
    path('login-user-bl/',LoginUser.as_view(),name="LoginUser"),
    path('logout-user/',LogoutUser.as_view(),name="LogoutUser"),

    #render ui related routes
    path('',register_user_page,name="register_user_page"),
    path('login-user/',login_user_page,name="login_user_page"),
]
