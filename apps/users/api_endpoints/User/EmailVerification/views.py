from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class ActivateAccountView(APIView):
    def get(self, request, token):
        user = get_object_or_404(CustomUser, activation_token=token)
        user.is_active = True
        user.activation_token = ''
        user.save()
        return Response({'message': 'Account activated successfully'}, status=status.HTTP_200_OK)


__all__ = ('ActivateAccountView',)
