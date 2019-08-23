from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from main.models import FavoriteThing, Category
from main.factories import BaseViewTest
from rest_framework import serializers

class FavouriteModelTestCase(BaseViewTest):
    def test_str(self):
        """Test for string representation."""

        favourite_thing = FavoriteThing.objects.get(title='samsung')
        self.assertEqual(
            str(favourite_thing),favourite_thing.title)




class FavouriteViewSetTestCase(BaseViewTest):
    def test_create_favourite_thing_pass(self):
        """POST to create a favourite thing."""
        data = {
            "title":"nokia",
            "ranking": 1,
            "category":self.category_one.category_name,
            }
       
        response = self.client.post(reverse('favourite-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'nokia')
        self.assertEqual(response.data['ranking'], 1)
        
    def test_create_favourite_thing_duplicate_fail(self):
        """POST to create a favourite thing."""
        data = {
            "title":"samsung",
            "ranking": 1,
            "category":self.category_one.category_name,
            }
       
        response = self.client.post(reverse('favourite-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(serializers.ValidationError)
        
        
    def test_favorite_thing_ranked_next_number_when_number_does_not_exist_pass(self):
        """
        Test that ranking is ordered
        """
        data = {
            "title":"techno",
            "ranking": 200,
            "category":self.category_one.category_name,
            }
        
        response = self.client.post(reverse('favourite-list'), data)
        self.assertEqual(response.data['ranking'], 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_favorite_thing_ranked_next_when_number_does_not_exist_pass(self):
        """
        Test that ranking is ordered
        """
        data = {
            "title":"techno",
            "ranking": 100,
            "category":self.category_two.category_name,
            }
        
        response = self.client.post(reverse('favourite-list'), data)
        self.assertEqual(response.data['ranking'], 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_favorite_thing_ranked_first_in_empty_category_when_number_does_not_exist_pass(self):
        """
        Test that ranking is ordered
        """
        data = {
            "title":"techno",
            "ranking": 100,
            "category":self.category_three.category_name,
            }
        
        response = self.client.post(reverse('favourite-list'), data)

        print('#################', response.data)
        self.assertEqual(response.data['ranking'], 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_favorite_thing_ranking_reordered_when_number_already_exist_pass(self):
        """
        Test that ranking is ordered
        """
        data = {
            "title":"finix",
            "ranking": 1,
            "category":self.category_one.category_name,
            }
        
        response = self.client.post(reverse('favourite-list'), data)
        self.assertEqual(response.data['ranking'], 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_favourite_things_pass(self):
        """
        GET  to create favourite things
        """
        response = self.client.get(reverse('favourite-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
    
    def test_list_one_favourite_thing_pass(self):
        """
        GET to create a favourite thing
        """

        response = self.client.get(reverse('favourite-detail', None, {self.favourite_thing_one.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_update_favourite_thing_pass(self):
        """
         UPDATE a favourite thing
        """
        data = {
            "title":"infinix",
            "ranking": 1,
            "category":self.category_one.category_name,
            }
        response = self.client.put(
            reverse('favourite-detail',
                    None, {self.favourite_thing_one.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'infinix')
    

    def test_update_favourite_thing_ranking_with_number_not_in_sequence_return_instance_pass(self):
        """
         UPDATE a favourite thing
        """
        data = {
            "title":"infinix",
            "ranking": 3,
            "category":self.category_one.category_name,
            }
        response = self.client.put(
            reverse('favourite-detail',
                    None, {self.favourite_thing_one.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'infinix')
        self.assertEqual(response.data['ranking'], 1)
    
    def test_update_favourite_thing_ranking_reorders_when_new_rank_is_greater_pass(self):
        """
         UPDATE a favourite thing
        """
        data = {
            "title":"infinix",
            "ranking": 2,
            "category":self.category_one.category_name,
            }
        response = self.client.put(
            reverse('favourite-detail',
                    None, {self.favourite_thing_one.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'infinix')
        self.assertEqual(response.data['ranking'], 2)
    

    def test_update_favourite_thing_ranking_reorders_when_new_rank_is_less_pass(self):
        """
         UPDATE a favourite thing
        """
        data = {
            "title":"infinix",
            "ranking": 1,
            "category":self.category_one.category_name,
            }
        response = self.client.put(
            reverse('favourite-detail',
                    None, {self.favourite_thing_one.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'infinix')
        self.assertEqual(response.data['ranking'], 1)
    
    def test_favorite_things_delete(self):
        """
         DELETE a favourite thing
        """
       
        response = self.client.delete(
            reverse('favourite-detail',
                    None, {self.favourite_thing_four.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
   
    def test_list_a_favourite_things_pass(self):
        """
        GET  to a favourite thing
        """
        response = self.client.get(reverse('favourite-detail', None, {self.favourite_thing_one.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_favorite_things_logs(self):
        """
        GET a favourite thing logs
        """
       
        response = self.client.get(
            reverse('favourite-logs',
                    None, {self.favourite_thing_four.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['logs'], [])
        