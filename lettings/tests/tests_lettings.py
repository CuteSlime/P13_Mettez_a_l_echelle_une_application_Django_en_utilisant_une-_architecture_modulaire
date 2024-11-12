import pytest

from django.urls import reverse

from lettings.models import Letting


@pytest.mark.django_db
def test_code_200_lettings_index(client, sample_data):
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert "<title>Lettings</title>" in response.content.decode()


@pytest.mark.django_db
def test_code_200_letting(client, sample_data):

    letting = Letting.objects.filter(id=1).first()
    assert letting is not None, "Letting with id=1 does not exist in the test data."

    response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
    assert response.status_code == 200
    assert f"<title>{letting.title}</title>" in response.content.decode()


@pytest.mark.django_db
def test_code_404_letting(client, sample_data):

    letting = Letting.objects.filter(id=99).first()
    assert letting is None, "Letting with id=99 exist in the test data."

    response = client.get(reverse("letting", kwargs={"letting_id": 99}))
    assert response.status_code == 404
    assert "<title>404</title>" in response.content.decode()
