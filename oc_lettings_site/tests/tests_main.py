import pytest


from django.urls import reverse


@pytest.mark.django_db
def test_code_200_oc_lettings_site(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in response.content.decode()
