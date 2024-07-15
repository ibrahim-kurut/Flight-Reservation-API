from django.urls import path

from .views import Register, UsersInfo




urlpatterns = [
    path('register/', Register.as_view()), # register endpoint = api/users/register/
    path('userinfo/', UsersInfo.as_view()),    # api/users/userinfo/
]