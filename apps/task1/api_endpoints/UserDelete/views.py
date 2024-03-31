from rest_framework.views import APIView
from apps.task1.models import User
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status


class UserDeleteAPIView(APIView):
    def post(self, request, token):
        user = get_object_or_404(User, token=token)
        user.is_active = False
        user.save()
        return Response(data={"detail": "deleted"}, status=status.HTTP_204_NO_CONTENT)


__all__ = [
    "UserDeleteAPIView",
]
