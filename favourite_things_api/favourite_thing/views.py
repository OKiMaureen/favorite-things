from django.shortcuts import render

# Create your views here.
from main.models import FavoriteThing
from django.db import IntegrityError
from main.serializers import FavouriteSerializer
from rest_framework import mixins, viewsets 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import  action
from .ranking_helper import reorder_rankings_subtract
from datetime import datetime
from dateutil.parser import parse

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
    
    @action(methods=['GET'],detail=True)
    def logs(self, request, pk=None):
        favourites_log = FavoriteThing.history.filter(id=pk)
        change_array = []
        response = []
        for i in range(0, len(favourites_log) - 1):
            new_record, old_record =  favourites_log[i], favourites_log[i + 1]
            delta = new_record.diff_against(old_record)
            change_array = change_array + delta.changes
        for change in change_array:
            change.field = change.field.title() 
            if change.field == 'Updated_At':
               
                new_date_str = parse(change.new).strftime("%d %B %Y, %H:%M:%S")

                response.append("Data was {} at {}".format('Modified', new_date_str))
            else:
                response.append(f"The field '{change.field}' changed from '{change.old}' to '{change.new}' ")
    
        return Response({
            "logs": response
        })
