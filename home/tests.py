from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Users

class ModelTestCase(TestCase):
	def setup(self):
		self.username = "write world class code"
		self.user = Users(uname=self.username)

	class ViewTestCase(TestCase):
    """Test suite for the api views."""

    	def setUp(self):
        """Define the test client and other test variables."""
        	self.client = APIClient()
        	self.user_data = {'uname': 'Go to Ibiza'}
        	self.response = self.client.post(
            	reverse('create'),
           		self.user_data,
            	format="json")

    	def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
       		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

		def test_model_can_create_a_bucket_list(self):
			old_count = Users.objects.count()
			self.user.save()
			new_count = Users.objects.count()
			self.assertNotEqual(old_count, new_count)
		
		