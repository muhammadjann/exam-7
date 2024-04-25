from rest_framework import serializers

from apps.najot.models import Teacher


class TeacherRetriveUpdateDestroySerializer(serializers.ModelSerializer):
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
