import pytest
from apps.users.models import User


@pytest.mark.django_db
def test_user_fixture(user):
    assert User.objects.filter(username='teste').exists()
