from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from main.models import Category
from .factories import CategoryFactory


class CategoryModelTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        category = CategoryFactory()
        self.assertEqual(str(category), category.category_name)




class CategoryViewSetTestCase(APITestCase):
    def test_create_category_pass(self):
        """POST to create a Category."""
        data = {
            'category_name': 'place',
        }
        self.assertEqual(Category.objects.count(), 0)
        response = self.client.post(reverse('category-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(category, field_name), data[field_name])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['category_name'], 'place')
        


    def test_list_category(self):
        """LIST categories."""
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        
