from main.models import Category
from django.db import IntegrityError
from main.serializers import CategorySerializer
from rest_framework import mixins, viewsets 
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class CategoryViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    