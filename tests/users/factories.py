import factory
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User
        
    email = fake.simple_profile()['mail']
    password = "testpass1234"