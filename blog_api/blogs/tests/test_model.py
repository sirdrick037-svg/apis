from django.contrib.auth import get_user_model
from django.test import TestCase
import datetime

from blogs.models import Blog

user = get_user_model()

class BlogModelTest(TestCase):
    def setUp(self):
        self.author = user.objects.create_user(
            email= "cedrick@example.com",
            password= "StrongPassword123!"
        )
    def test_post_generate_slug_from_title(self):
        post = Blog.objects.create(
            author=self.author,
            title="Learning Django Testing",
            text="Testing Django Applicatins",
            published_date= datetime.datetime.now()
        )    
        self.assertEqual(
            post.slug,
            "learning-django-testing",
        )

        
        