from django.shortcuts import render

# Create your views here.
from main.models import FavoriteThing
from django.db import IntegrityError
from main.serializers import FavouriteSerializer
from rest_framework import mixins, viewsets 
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .ranking_helper import reorder_rankings_subtract


# Create your views here.

class FavouriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavouriteSerializer
    queryset = FavoriteThing.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        queryset = self.get_queryset()
        next_rankings = queryset.filter(ranking__gt=instance.ranking)
        reorder_rankings_subtract(next_rankings)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    