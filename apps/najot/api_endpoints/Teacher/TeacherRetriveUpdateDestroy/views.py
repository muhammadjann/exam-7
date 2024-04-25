from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.najot.api_endpoints.Teacher.TeacherRetriveUpdateDestroy.serializers import (
    TeacherRetriveUpdateDestroySerializer,
)
from apps.najot.models import Teacher
from apps.najot.permissions import IsOwnerOrReadOnly


class TeacherRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherRetriveUpdateDestroySerializer
    permission_classes = [
        IsOwnerOrReadOnly,
    ]


__all__ = ["TeacherRetriveUpdateDestroyView"]
