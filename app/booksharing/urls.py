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

    path('accounts/my-profile/', MyProfileView.as_view(), name='my-profile'),


]
