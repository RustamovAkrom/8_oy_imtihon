from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            logout(request)
            request.user.auth_token.delete()
            return Response(
                {"detail": "Successfully logged out"}, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"detail": "User hast no credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )


__all__ = [
    "UserLogoutAPIView",
]
