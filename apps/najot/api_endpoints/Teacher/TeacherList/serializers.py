from apps.najot.api_endpoints.Course.CourseCreate import serializers
from apps.najot.models import Teacher


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "age",
            "degree",
            "email",
            "image",
        ]
