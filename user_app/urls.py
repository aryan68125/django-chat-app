from django.urls import path

from user_app.views import test
urlpatterns = [
    path('test/',test.as_view(),name="test"),
]
