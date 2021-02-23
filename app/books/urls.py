from django.urls import path
from books import views

app_name = "books"

urlpatterns = [
    path('list/', views.BookList.as_view(), name='list'),
    path('create/', views.BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='delete'),
]