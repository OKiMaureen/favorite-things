from factory import DjangoModelFactory, Faker

from main.models import Category


class CategoryFactory(DjangoModelFactory):
    category_name = Faker('city')

    class Meta:
        model = Category
