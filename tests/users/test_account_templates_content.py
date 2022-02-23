import pytest
from django.urls import reverse_lazy


@pytest.mark.django_db
def test_login_page_content(client):
    url = reverse_lazy("account_login")
    assert "Login" in str(client.get(url).content)


@pytest.mark.django_db
def test_signup_page_content(client):
    url = reverse_lazy("account_signup")
    assert "Signup" in str(client.get(url).content)
