from django.urls import path, include
from .views import BlogViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
#     path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
#     path('blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
#     path('authors/', AuthorListAPIView.as_view(), name='author-list'),
      path('', include(router.urls)),
      path('schema/', SpectacularAPIView.as_view(), name='schema'),
      path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
      path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]    
