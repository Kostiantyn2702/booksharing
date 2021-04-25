from books.api import views
from rest_framework.routers import DefaultRouter

app_name = 'books-api'

router = DefaultRouter()

router.register('books', views.BookModelViewSet, basename='book')
router.register('author', views.AuthorModelViewSet, basename='author')
router.register('category', views.CategoryModelViewSet, basename='category')


urlpatterns = router.urls
