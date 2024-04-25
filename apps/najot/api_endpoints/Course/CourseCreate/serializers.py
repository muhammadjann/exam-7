from rest_framework.serializers import ModelSerializer

from apps.najot.models import Course


class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "duration",
            "description",
        ]
