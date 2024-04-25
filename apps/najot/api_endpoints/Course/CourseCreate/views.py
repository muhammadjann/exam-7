from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.najot.api_endpoints.Course.CourseCreate.serializers import (
    CourseCreateSerializer,
)
from apps.najot.models import Course
from apps.najot.permissions import IsOwnerOrReadOnly


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["CourseCreateAPIView"]
