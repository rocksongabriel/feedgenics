import pytest
from users.admin import UserCreationForm


@pytest.mark.django_db
def test_admin_user_creation_form():
    data = {
        "email": "test@test.com",
        "password1": "testpass1234",
        "password2": "testpass1234",
    }
    form = UserCreationForm(data=data)
    if form.is_valid():
        form.save()
    assert form.is_bound
    assert form.is_valid()
    
# TODO - test the ValidationError