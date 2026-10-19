
import datetime

from django.contrib.auth import get_user_model

from blogs.models import Author, Blog

User = get_user_model()

DEFAULT_PASSWORD = "StrongPassword123!"


def make_user(email, **extra):
    """Create a user. Each test must use a different username."""
    return User.objects.create_user(
        email=email,
        password=DEFAULT_PASSWORD,
        **extra,
    )


def make_author(user):
    """Create an Author linked to a user.

    Change this function if your Author model has different fields.
    """
    return Author.objects.create(user=user)


def make_blog(author, **overrides):
    """Create a Blog with sensible defaults.

    Pass keyword arguments to override any field, for example:
        make_blog(author, is_published=False)
    """
    data = {
        "title": "Learning Django Testing",
        "text": "Testing Django applications.",
        "published_date": datetime.date(2026, 1, 15),
    }
    data.update(overrides)
    return Blog.objects.create(author=author, **data)


def results_from(response):
    """Return the list of items from a DRF list response.

    Works whether or not pagination is switched on.
    """
    data = response.data
    if isinstance(data, dict) and "results" in data:
        return data["results"]
    return data