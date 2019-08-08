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

    def create(self, request, *args, **kwargs):
        data = {'category_name': request.data.get('category_name', '').lower()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        category_name = serializer.validated_data.get('category_name')

        category_exists = Category.objects.filter(category_name=category_name)
        if category_exists:
            return Response({
                'message': 'Category already exist'
            }, status=status.HTTP_409_CONFLICT)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['GET'],detail=True)
    def favourite_things(self, request, pk=None):
        favourites = FavoriteThing.objects.filter(category_id=pk)
        serializer = FavouriteSerializer(
                 favourites, many=True
            )
        return Response(serializer.data, status=status.HTTP_200_OK)

