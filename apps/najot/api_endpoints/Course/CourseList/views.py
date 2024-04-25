from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from apps.najot.api_endpoints.Course.CourseList.serializers import CourseListSerializer
from apps.najot.models import Course


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ("name", "category__name", "type")
    ordering_fields = ("name", "category__name", "type", "duration")


__all__ = ["CourseListView"]
