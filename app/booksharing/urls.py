import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path
from accounts.views import MyProfileView, ContactUsView, SignUpView, ActivateView
from books import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


API_V1_PREFIX = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),

    path('', views.Index.as_view(), name='index'),

    path('accounts/my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('accounts/contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/activate/<uuid:username>/<token>/', ActivateView.as_view(), name='activate'),

    # API
    path(API_V1_PREFIX, include('books.api.urls')),
    path(f'{API_V1_PREFIX}token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_V1_PREFIX}token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    import debug_toolbar # noqa

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
