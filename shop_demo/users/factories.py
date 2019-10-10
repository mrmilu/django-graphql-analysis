# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports
import factory

# App imports
from shop_demo.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
