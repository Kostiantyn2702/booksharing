"""booksharing URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('books/list/', views.book_list, name='books-list'),
    path('books/create/', views.book_create, name='books-create'),
    path('books/update/<int:pk>/', views.book_update, name='books-update'),
    path('books/delete/<int:pk>/', views.book_delete, name='books-delete'),

    # path('books/author/list/', views.author_list, name='author-list'),
    # path('books/author/create/', views.author_create, name='author-create'),
    # path('books/author/update/<int:pk>/', views.author_update, name='author-update'),
    # path('books/author/delete/<int:pk>/', views.author_delete, name='author-delete'),
]
