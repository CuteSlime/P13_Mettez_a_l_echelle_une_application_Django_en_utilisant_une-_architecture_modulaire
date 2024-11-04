import pytest

from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_code_200_profiles_index(client, sample_data):
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200
    assert "<title>Profiles</title>" in response.content.decode()


@pytest.mark.django_db
def test_code_200_profile(client, sample_data):

    profile = Profile.objects.filter(id=1).first()
    assert profile is not None, "Profile with id=1 does not exist in the test data."

    response = client.get(reverse("profile", kwargs={"username": profile.user.username}))
    assert response.status_code == 200
    assert f"<title>{profile.user.username}</title>" in response.content.decode()
