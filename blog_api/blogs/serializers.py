from rest_framework import serializers
from .models import Author, Blog

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(source='author', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'text', 'author', 'author_name', 'published_date', 'created_at']