from django.urls import path
from books import views

app_name = "books"

urlpatterns = [
    # book
    path('list/', views.BookList.as_view(), name='list'),
    path('list/my-books/', views.MyBooksList.as_view(), name='my-books'),
    path('create/', views.BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='delete'),

    # author
    path('author/list/', views.AuthorList.as_view(), name='author-list'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),
]
