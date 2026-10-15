from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet,
    TeacherViewSet,
    StudentViewSet,
    CourseViewSet,
    EnrollmentViewSet
)
router = DefaultRouter()

router.register('departments',DepartmentViewSet, basename='departments')
router.register('teachers',TeacherViewSet, basename='teachers')
router.register('students',StudentViewSet, basename='students')
router.register('courses',CourseViewSet, basename='courses')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    
]
