from django.db import models

from apps.shared.models import AbstractModel
from apps.users.models import User


class Category(AbstractModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        db_table = "category"


class Course(AbstractModel):
    TYPE_CHOICE = [
        ("standard", "Standard"),
        ("bootcamp", "Bootcamp"),
        ("online", "Online"),
    ]

    name = models.CharField(max_length=50)
    category = models.ManyToManyField("Category", related_name="subjects")
    teacher = models.ForeignKey(
        "Teacher", on_delete=models.CASCADE, related_name="subjects"
    )
    duration = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="courses/", null=True, blank=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICE, default="s")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.name} | {self.type}"

    class Meta:
        verbose_name_plural = "Courses"
        verbose_name = "Course"
        db_table = "course"
        ordering = ["name"]


class Teacher(AbstractModel):
    Degree = [
        ("middle", "Middle"),
        ("senior", "Senior"),
        ("master", "Master"),
        ("academic", "Academic"),
    ]

    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    degree = models.CharField(max_length=9, choices=Degree)
    image = models.ImageField(upload_to="teachers/", null=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teachers")

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        db_table = "teacher"

    def __str__(self):
        return "{0}{1}".format(self.first_name, self.last_name)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
