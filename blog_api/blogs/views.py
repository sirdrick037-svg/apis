from rest_framework import viewsets, filters

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, exceptions
# from django.db import IntegrityError
from rest_framework import AllowAny
from .models import Blog, Author
from .serializers import BlogSerializer, AuthorSerializer
from drf_spectacular.utils import extend_schema
class AuthorViewSet(viewsets.ModelViewSet):
    """""
    A viewset that returns all the authors
    """""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @extend_schema(
        summary="Retrieve all users",
        description="This endpoint returns all active users in the system.",
        responses=AuthorSerializer(many=True)
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.select_related('author').all()
    serializer_class = BlogSerializer  

      
#1. Enable specific filters for this viewset
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # 2. Define which fields act as text searches
    search_fields = ['title', 'text', 'author__first_name', 'author__last_name']
    
    # 3. Define which fields clients are allowed to sort by
    ordering_fields = ['published_date', 'created_at', 'title']
    
    # 4. (Optional) Provide a default ordering
    ordering = ['-published_date']

# class BlogListCreateAPIView(APIView):
#     def get(self, request):
#         blogs = Blog.objects.select_related('author').all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except IntegrityError:
#                 print("serializer.data", serializer.data)
#                 return Response({"detail": "Invalid data."}, status=status.HTTP_409_CONFLICT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BlogDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise exceptions.NotFound(f"Blog with ID {pk} not found.")

#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data)
#             except IntegrityError:
#                 return Response({"detail": "Invalid data."}, status=status.HTTP_409_CONFLICT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class AuthorListAPIView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)