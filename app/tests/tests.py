from django.urls import reverse


def test_sanity():
    assert 200 == 200


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert response.template_name == ['index.html']
