from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from apps.task1.models import User
from rest_framework.response import Response


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(data={"detail": "Logged in successfully!"})
            else:
                return Response(data={"detail": "is are not active!"})
        else:
            return Response(data={"detail": "User does not exist!"})


__all__ = [
    "UserLoginAPIView",
]
