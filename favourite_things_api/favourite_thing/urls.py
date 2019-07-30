
from django.conf.urls import url
from django.urls import path
from rest_framework.routers import SimpleRouter
from favourite_thing.views import FavouriteViewSet


router = SimpleRouter()
router.register(r'favourite', FavouriteViewSet, base_name='favourite')


urlpatterns = router.urls
