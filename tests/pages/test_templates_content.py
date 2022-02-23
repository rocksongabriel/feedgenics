import pytest
from django.urls import reverse_lazy

def test_homepage_content(client):
    url = reverse_lazy('pages:homepage')
    assert 'Subscribe' in str(client.get(url).content)