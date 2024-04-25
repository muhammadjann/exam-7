from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.najot.api_endpoints.Teacher.TeacherCreate.serializers import (
    TeacherCreateSerializer,
)
from apps.najot.models import Teacher


class TeacherCreateAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer
    permission_classes = [
        IsAuthenticated,
    ]


__all__ = ["TeacherCreateAPIView"]
