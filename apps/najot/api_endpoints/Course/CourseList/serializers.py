from rest_framework.serializers import ModelSerializer

from apps.najot.models import Course


class CourseListSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
