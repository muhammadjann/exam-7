from rest_framework import serializers

from apps.najot.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "name",
            "category",
            "teacher",
            "duration",
            "description",
            "type",
            "image",
        ]
