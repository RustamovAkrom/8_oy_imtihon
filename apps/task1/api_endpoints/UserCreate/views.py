from rest_framework.generics import CreateAPIView
from apps.task1.models import User
from .serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


__all__ = [
    "UserCreateAPIView",
]
