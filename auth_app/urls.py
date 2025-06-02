from django.urls import path

from auth_app.views_bl import RegisterUser
from auth_app.views import register_user_page
urlpatterns = [
    # business logic realted routes
    path('resgister-user/',RegisterUser.as_view(),name="RegisterUser"),

    #render ui related routes
    path('',register_user_page,name="register_user_page"),
]
