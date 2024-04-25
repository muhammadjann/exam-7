from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from apps.najot.api_endpoints.Teacher.TeacherList.serializers import (
    TeacherListSerializer,
)
from apps.najot.models import Teacher


class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        "first_name",
        "last_name",
    )
    ordering_fields = ("first_name", "last_name", "degree")


__all__ = ["TeacherListAPIView"]
