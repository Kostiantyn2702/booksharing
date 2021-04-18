from django.urls import reverse
from accounts.models import User


def login_user(client):
    login_url = reverse('login')

    # create user
    password = 'helloWorld123'
    email = 'test_login_success@mail.com'
    avatar = 'avatars/47/IMG_20210320_000433.jpg'
    user = User(email=email, username=email, avatar=avatar)
    user.set_password(password)
    user.save()

    payload = {
        'username': email,
        'password': password,
    }
    client.post(login_url, data=payload)
    return user


def test_get_form(client):
    url = reverse('my-profile')
    login_user(client)
    response = client.get(url, follow=True)

    assert response.status_code == 200


def test_empty_payload(client):
    url = reverse('my-profile')
    login_user(client)
    payload = {}
    response = client.put(url, data=payload, follow=True)

    assert response.status_code == 200
    assert response.redirect_chain == [('/', 302)]


def test_valid_payload(client):
    url = reverse('my-profile')
    login_user(client)
    payload = {"first_name": "test",
               "last_name": "test",
               "avatar": 'avatars/47/IMG_20210320_000433.jpg'}
    response = client.put(url, data=payload, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain == [('/', 302)]
