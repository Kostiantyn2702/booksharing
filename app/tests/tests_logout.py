from django.urls import reverse
from accounts.models import User


def test_logout_success(client):
    url_login = reverse('login')
    url_logout = reverse('logout')
    url_my_profile = reverse('my-profile')

    # logined user
    password, email, avatar = ('helloWorld123',
                               'test_login_success@mail.com',
                               'avatars/47/IMG_20210320_000433.jpg',)
    user = User(email=email, username=email, avatar=avatar)
    user.set_password(password)
    user.save()
    payload = {
        'username': email,
        'password': password,
    }
    client.post(url_login, data=payload)

    # 1 Chek that User is login
    response = client.get(url_my_profile)
    assert response.status_code == 200

    # 2 Logout button
    response = client.get(url_logout)
    assert response.status_code == 302

    # 3 User is logout
    client.post(url_logout)
    response = client.get(url_my_profile)
    assert response.status_code == 302
