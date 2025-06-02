from django.contrib import path
from auth_app.views_bl import RegisterUser
urlpatterns = [
    path('resgister-user/',RegisterUser.as_view(),name="RegisterUser"),
]
