from django.urls import path
from .api_endpoints.UserCreate import UserCreateAPIView
from .api_endpoints.UserDelete import UserDeleteAPIView
from .api_endpoints.UserLogin import UserLoginAPIView
from .api_endpoints.UserLogout import UserLogoutAPIView
from .api_endpoints.UserList import UserListAPIView


app_name = "task1"
urlpatterns = [
    path("user-logout/", UserLogoutAPIView.as_view(), name="user-logout"),
    path("user-login", UserLoginAPIView.as_view(), name="user-login"),
    path("user-create/", UserCreateAPIView.as_view(), name="user-create"),
    path("user-delete/<str:token>", UserDeleteAPIView.as_view(), name="user-delete"),
    path("user-list", UserListAPIView.as_view(), name="user-list"),
]
