from main.models import Category, FavoriteThing
from django.db import IntegrityError
from main.serializers import CategorySerializer, FavouriteSerializer
from rest_framework import mixins, viewsets
from rest_framework.decorators import  action
from rest_framework import status
from rest_framework.response import Response




# Create your views here.

class CategoryViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    @action(methods=['GET'],detail=True)
    def favourite_things(self, request, pk=None):
        favourites = FavoriteThing.objects.filter(category_id=pk)
        serializer = FavouriteSerializer(
                 favourites, many=True
            )
        return Response(serializer.data)
