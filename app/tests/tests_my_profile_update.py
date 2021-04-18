from django.urls import reverse


def test_get_form(client):
    url = reverse('my-profile')
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain == [('/accounts/login/?next=/accounts/my-profile/', 302)]


def test_empty_payload(client):
    url = reverse('my-profile')
    payload = {}
    response = client.patch(url, data=payload, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain == [('/accounts/login/?next=/accounts/my-profile/', 302)]


def test_valid_payload(client):
    url = reverse('my-profile')
    payload = {"first_name": "first_name",
               "last_name": "last_name"}
    response = client.patch(url, data=payload, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain == [('/accounts/login/?next=/accounts/my-profile/', 302)]
