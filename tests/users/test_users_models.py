import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user(new_user):
    """Test the creation of a new user object"""
    user = User.objects.create_user(email=new_user.email, password=new_user.password)

    assert str(user) == user.email
    assert User.objects.count() == 1
    assert user.email
    assert user.is_active
    assert user.is_staff is False
    assert user.is_admin is False
    assert user.is_superuser is False


@pytest.mark.django_db
def test_createsuper_user(new_user):
    """Test the creation of a new superuser object"""
    superuser = User.objects.create_superuser(
        email=new_user.email, password=new_user.password
    )

    assert str(superuser) == superuser.email
    assert User.objects.count() == 1
    assert superuser.email
    assert superuser.is_active
    assert superuser.is_staff
    assert superuser.is_admin
    assert superuser.is_superuser


# TODO - test the line that raises ValueError
