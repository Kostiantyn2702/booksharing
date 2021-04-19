from django.urls import reverse
from books.models import Author, Book
from accounts.models import User
import pytest


# author create
def create_author():
    first_name = "first_name"
    last_name = "last_name"
    country = "country"
    gender = "gender"
    native_language = "native_language"
    author = Author(first_name=first_name,
                    last_name=last_name,
                    country=country,
                    gender=gender,
                    native_language=native_language)
    author.save()
    return author


# book create
@pytest.mark.django_db
def create_book(client):
    author = create_author()
    title = "title"
    publish_year = 1993
    review = "eifh"
    condition = 1
    book = Book(author=author,
                title=title,
                publish_year=publish_year,
                review=review,
                condition=condition,
                user=client)
    book.save()
    return book


@pytest.mark.django_db
def test_get_form(client):
    url = reverse('books:list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_books_list_for_login_user(client):
    login_url = reverse('login')
    url_logout = reverse('logout')
    book_list_url = reverse('books:list')
    create_book_url = reverse('books:create')

    # create some books from other people
    user = None
    create_book(user)
    create_book(user)

    # create user
    password = 'helloWorld123'
    email = 'test_login_success@mail.com'
    avatar = 'avatars/47/IMG_20210320_000433.jpg'
    login_user = User(email=email, username=email, avatar=avatar)
    login_user.set_password(password)
    login_user.save()

    # login user
    payload = {
        'username': email,
        'password': password,
    }
    client.post(login_url, data=payload)
    create_book(login_user)

    # add book from login user
    author = create_author()
    payload = {"author": author,
               "title": "title2",
               "publish year": 1290,
               "review": "eifh",
               "condition": 1,
               "coverage": 'avatars/47/IMG_20210320_000433.jpg'}
    client.put(create_book_url, data=payload)

    # books list for login user
    queryset_for_login_user = Book.objects.exclude(user=login_user)
    response = client.get(book_list_url)
    assert str(response.context_data['book_list']) == str(queryset_for_login_user)
    assert response.status_code == 200

    # books list for annon user
    queryset_for_anon = Book.objects.all()
    client.get(url_logout)
    response = client.get(book_list_url)
    assert str(response.context_data['object_list']) == str(queryset_for_anon)
    assert response.status_code == 200
