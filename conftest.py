import pytest
from apps.users.models import User


@pytest.fixture
def user():
    return User.objects.create_user(username='teste', password='senha123')
