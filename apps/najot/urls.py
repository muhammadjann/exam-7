from django.urls import path
from apps.najot.api_endpoints.Course import (
    CourseListView,
    CourseCreateAPIView,
    CourseRetriveUpdateDestroyView,
)
from apps.najot.api_endpoints.Teacher import (
    TeacherListAPIView,
    TeacherCreateAPIView,
    TeacherRetriveUpdateDestroyView,
)

urlpatterns = [
    path("course/", CourseListView.as_view()),
    path("course/create", CourseCreateAPIView.as_view()),
    path("course/<pk>/", CourseRetriveUpdateDestroyView.as_view()),
    path("teacher/", TeacherListAPIView.as_view()),
    path("teacher/create", TeacherCreateAPIView.as_view()),
    path("teacher/<pk>/", TeacherRetriveUpdateDestroyView.as_view()),
]
