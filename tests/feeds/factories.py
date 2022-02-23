import factory
from faker import Faker
import datetime
from django.utils import timezone
from tests.users.factories import UserFactory

from feeds.models import Entry, Feed

fake = Faker()


class FeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Feed

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker("sentence")
    created = timezone.now()
    link = "https://upwork.com"
    number_of_update_posts = 4
    email = fake.simple_profile()["mail"]


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    feed = factory.SubFactory(FeedFactory)
    published = timezone.now()
    title = factory.Faker("sentence")
    link = "https://upwork.com/job-post/"
    summary = factory.Faker("text")
    emailed = True
