import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from accounts.views import MyProfileView
from books import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),

    path('', views.Index.as_view(), name='index'),

    path('__debug__/', include(debug_toolbar.urls)),

    path('books/author/list/', views.author_list, name='author-list'),
    path('books/author/create/', views.author_create, name='author-create'),
    path('books/author/update/<int:pk>/', views.author_update, name='author-update'),
    path('books/author/delete/<int:pk>/', views.author_delete, name='author-delete'),


    path('accounts/my-profile/', MyProfileView.as_view(), name='my-profile'),


]
