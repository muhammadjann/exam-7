from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class ChangePasswordView(APIView):
    permission_classes = (JWTAuthentication,)

    def post(self, request):
        user = request.user
        data = request.data

        old_password = data.get("old_password")
        new_password = data.get("new_password")

        if not old_password or not new_password:
            return Response(
                {"error": "Please provide both old and new passwords"}, status=400
            )

        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect"}, status=400)

        user.set_password(
            new_ppath(
                "api/token/verify/", TokenVerifyView.as_view(), name="token_verify"
            ),
            assword,
        )
        user.save()

        return Response({"message": "Password changed successfully"}, status=200)


class PasswordResetRequest(APIView):
    def post(self, request):
        email = request.data.get("email")
        user = get_object_or_404(User, email=email)

        new_password = get_random_string(length=10)
        user.set_password(new_password)
        user.save()

        send_mail(
            "Password Reset",
            f"Your new password is: {new_password}",
            "muhammadboriyev5889@gmail.com",
            [user.email],
        )

        return Response(
            {
                "message": "Password reset successful. Check your email for the new password."
            },
            status=status.HTTP_200_OK,
        )


__all__ = ["ChangePasswordView", "PasswordResetRequest"]
