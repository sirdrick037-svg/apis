from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.
from .models import (
    Department,
    Teacher,
    Student,
    Course,
    Enrollment,
)

from .serializers import (
    DepartmentSerializer,
    TeacherSerializer,
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("name")
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related(
        "department"
    ).all().order_by("last_name")
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("last_name")
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related(
        "department"
    ).prefetch_related("teachers").all().order_by("code")
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related(
        "student",
        "course",
    ).all().order_by("-enrolled_on")
    serializer_class = EnrollmentSerializer
    permission_classes = [AllowAny]