import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from books import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('__debug__/', include(debug_toolbar.urls)),

    path('books/list/', views.book_list, name='books-list'),
    path('books/create/', views.book_create, name='books-create'),
    path('books/update/<int:pk>/', views.book_update, name='books-update'),
    path('books/delete/<int:pk>/', views.book_delete, name='books-delete'),

    path('books/author/list/', views.author_list, name='author-list'),
    path('books/author/create/', views.author_create, name='author-create'),
    path('books/author/update/<int:pk>/', views.author_update, name='author-update'),
    path('books/author/delete/<int:pk>/', views.author_delete, name='author-delete'),
]
