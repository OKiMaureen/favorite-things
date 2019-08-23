from rest_framework import serializers
from django.db.utils import IntegrityError
from .models import Category, FavoriteThing
from favourite_thing.ranking_helper import reorder_rankings_subtract

class FavouriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='category_name')
    class Meta:
        model = FavoriteThing
        fields = ['id', 'title', 'description', 'ranking','metadata','category','created_at','updated_at']
    

    def reorder_rankings_add(self, instance):
        for item in instance:
            item.ranking += 1
            item.save()
    

    def create(self, validated_data):
        ranking = validated_data.get('ranking')
        category = validated_data.get('category')
        rankings_queryset = FavoriteThing.objects.order_by('ranking').filter(category=category)
        existing_ranking = rankings_queryset.filter(ranking=ranking)

        if not rankings_queryset and ranking > 1:
            ranking = 1
            validated_data = {**validated_data, 'ranking': ranking}

        if rankings_queryset and \
                ranking > rankings_queryset.last().ranking + 1:
            ranking = rankings_queryset.last().ranking + 1
            validated_data = {**validated_data, 'ranking': ranking}

        if existing_ranking:
            next_rankings = rankings_queryset.filter(ranking__gte=ranking)
            self.reorder_rankings_add(next_rankings)
        try:
            favorite_thing = FavoriteThing.objects.create(**validated_data)
            return favorite_thing
        except IntegrityError:
            raise serializers.ValidationError('The Favorite thing already exists for this category')


    def update(self,  instance, validated_data):
        ranking = validated_data.get('ranking', instance.ranking)
        category = validated_data.get('category', instance.category)
        rankings_queryset = FavoriteThing.objects.order_by('ranking').filter(category=category)
        existing_ranking = rankings_queryset.filter(ranking=ranking)
        
        if not rankings_queryset and ranking > 1:
            ranking = 1
            validated_data = {**validated_data, 'ranking': ranking}

        if rankings_queryset and ranking >= rankings_queryset.last().ranking + 1:
            ranking = instance.ranking
            validated_data = {**validated_data, 'ranking': ranking}

        if existing_ranking:
        
            if ranking > instance.ranking:
                next_rankings = rankings_queryset.filter(
                    ranking__range=(instance.ranking+1, ranking))
                reorder_rankings_subtract(next_rankings)
            else:
                next_rankings = rankings_queryset.filter(
                    ranking__range=(ranking, instance.ranking-1))
                self.reorder_rankings_add(next_rankings)


        for name, value in validated_data.items():
            setattr(instance, name, value)
       
        try:
            instance.save()
            return instance
        except IntegrityError:
            raise serializers.ValidationError('The Favourite thing already exists for this category')



class CategorySerializer(serializers.ModelSerializer):
    favourite_things = FavouriteSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_at', 'updated_at', 'favourite_things']
    