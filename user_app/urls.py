from django.urls import path
from user_app.views import render_profile_page
from user_app.views_bl import ProcessUserProfileData
urlpatterns = [
    # business logic urls
    path('user_profile_settings/',ProcessUserProfileData.as_view(),name="ProcessUserProfileData"),

    # render page urls
    path('user_profile_page/',render_profile_page,name="render_profile_page"),
]
