
from django.conf.urls import url
from django.urls import path
from rest_framework.routers import SimpleRouter
from category.views import CategoryViewSet


router = SimpleRouter()
router.register(r'category', CategoryViewSet, base_name='category')


urlpatterns = router.urls
