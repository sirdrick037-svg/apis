from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import make_author, make_blog, make_user, results_from

class BlogListAPITest(APITestCase):
    def setUp(self):
        self.author = make_user("Kwanusujoseph@example.com", "StrongPassword")
        make_blog(self.author, title="This is a Test Title")
        make_blog(self.author, title="Private Draft", is_published=False)
        self.url = reverse("blog-list")
    def test_list_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    