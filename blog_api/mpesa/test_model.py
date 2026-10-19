from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Blog

user = get_user_model()

class BlogModelTest(TestCase):
    