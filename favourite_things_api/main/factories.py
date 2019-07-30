from rest_framework.test import APITestCase
from main.models import FavoriteThing, Category


class BaseViewTest(APITestCase):
    @staticmethod
    def create_category(category_name=''):
        category = Category.objects.create(category_name=category_name)
        return category
    
    @staticmethod
    def create_favorite_thing(**kwargs):
        favorite_thing = FavoriteThing.objects.create(**kwargs)
        return favorite_thing

    def setUp(self):
        self.category_one = self.create_category('phone')
        self.category_two = self.create_category('food')
        self.category_three = self.create_category('place')
        self.favourite_thing_one = self.create_favorite_thing(
            title='samsung', description='a good phone',
            ranking=1,
            metadata={"model": "A series"},
            category=self.category_one, 
        )
        self.favourite_thing_two = self.create_favorite_thing(
            title='rice', description='a good food',
            ranking=1,
            category=self.category_two, 
        )
        self.favourite_thing_three = self.create_favorite_thing(
            title='erricson', description='a good phone',
            ranking=2,
            metadata={"model": "A series"},
            category=self.category_one, 
        )
        self.favourite_thing_four = self.create_favorite_thing(
            title='beans', description='a good food',
            ranking=2,
            category=self.category_two, 
        )

    class Meta:
        model = FavoriteThing
