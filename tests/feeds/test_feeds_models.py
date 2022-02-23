import pytest
from feeds.models import Feed, Entry


def test_feed_model(new_feed):
    assert new_feed.created
    assert new_feed.link
    assert new_feed.number_of_update_posts
    assert new_feed.email
    assert str(new_feed) == new_feed.name
    assert Feed.objects.count() == 1


def test_entry_model(new_entry):
    assert new_entry.feed
    assert new_entry.published
    assert new_entry.title
    assert new_entry.link
    assert new_entry.summary
    assert new_entry.emailed
    assert str(new_entry) == new_entry.title
    assert Entry.objects.count() == 1
