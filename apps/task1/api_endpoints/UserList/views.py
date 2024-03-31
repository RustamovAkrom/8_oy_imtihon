from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.task1.models import User
from .serializers import UserListSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(is_active=True)
        return queryset


__all__ = [
    "UserListAPIView",
]
