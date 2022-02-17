import pytest
from django.contrib.auth import get_user_model
from pytest_factoryboy import register

from tests.users.factories import UserFactory

User = get_user_model()


# Register models
register(UserFactory)


@pytest.fixture
def new_user(user_factory):
    user_data = user_factory.build()
    return user_data