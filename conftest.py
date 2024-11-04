import pytest

from django.test import Client
from django.contrib.auth.models import User

from lettings.models import Address, Letting
from profiles.models import Profile


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def sample_data(db):
    user = User.objects.create(username="test_user", password="testPass")
    address = Address.objects.create(
        number="12", street="parla", city="paris", state="France", zip_code="90000", country_iso_code="033",)
    Letting.objects.create(title="Example 1", address=address)
    Profile.objects.create(user=user, favorite_city="Grenoble")
