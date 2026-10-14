from django.urls import path, include
from .views import BlogViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
#     path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
#     path('blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
#     path('authors/', AuthorListAPIView.as_view(), name='author-list'),
      path('v1/api/',include(router.urls)),
]    
