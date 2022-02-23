import pytest
from django.contrib.auth import get_user_model
from pytest_factoryboy import register

from tests.users.factories import UserFactory
from tests.feeds.factories import FeedFactory, EntryFactory

User = get_user_model()


# Register factories
register(UserFactory)

register(FeedFactory)
register(EntryFactory)


@pytest.fixture
def new_user(user_factory):
    user_data = user_factory.build()
    return user_data


@pytest.fixture
def new_feed(db, feed_factory):
    feed_data = feed_factory.create()
    return feed_data


@pytest.fixture
def new_entry(db, entry_factory):
    entry_data = entry_factory.create()
    return entry_data
