from django.urls import path
from home_app.views import render_home_page
urlpatterns = [
    path('home_page/',render_home_page,name="render_home_page"),
]
