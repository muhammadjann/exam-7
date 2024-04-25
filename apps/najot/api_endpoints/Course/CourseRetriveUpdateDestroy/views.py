from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.najot.api_endpoints.Course.CourseRetriveUpdateDestroy.serializers import (
    CourseSerializer,
)
from apps.najot.models import Course
from apps.najot.permissions import IsOwnerOrReadOnly


class CourseRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsOwnerOrReadOnly,)


__all__ = ["CourseRetriveUpdateDestroyView"]
