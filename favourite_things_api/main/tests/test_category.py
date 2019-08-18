from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from main.models import Category
from main.factories import BaseViewTest


class CategoryModelTestCase(BaseViewTest):
    def test_str(self):
        """Test for string representation."""
        
        category = Category.objects.get(category_name='phone')
        self.assertEqual(
            str(category),category.category_name)



class CategoryViewSetTestCase(BaseViewTest):
    def test_create_category_duplicate_category_fail(self):
        """POST to create a Category."""
        data = {
            'category_name': 'place',
        }
        response = self.client.post(reverse('category-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
       
        
        
    def test_create_category_pass(self):
        """POST to create a Category."""
        data = {
            'category_name': 'school',
        }
        response = self.client.post(reverse('category-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['category_name'], 'school')
        
        

    def test_list_category(self):
        """LIST categories."""
        
        response = self.client.get(reverse('category-list'))
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       

    def test_list_favourite_things_under_a_category(self):
        """LIST categories."""
        
        response = self.client.get(reverse('category-detail', None, {self.category_one.pk}))
        self.assertEqual(len(response.data['favourite_things']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
        
