from django.test import TestCase,Client
from django.urls import reverse,resolve
from hamcrest import assert_that, is_in, starts_with, has_items, equal_to, has_value

class testing(TestCase):
	def setUp(self):
		self.client = Client()
		self.username="he"
		self.password="he"

	def test_if_index_page_functional(self):
		url = reverse('index')
		assert_that(self.client.get(url).status_code,equal_to(200))

	def test_login_with_correct_username_password(self):
		url = reverse('login')
		assert_that(self.client.post(url,{'username':self.username,'password':self.password }).status_code,equal_to(302))
		
	def test_posting_a_blog(self):
		url = reverse('entry')
		assert_that(self.client.post(url,{'username':'sandeep','blog':'this is'}).url,'/entered')

	def test_delete_in_a_blog(self):
		url = reverse('login')
		self.client.post(url,{'username':'he','password':'he'})
		url = reverse('entry')
		self.client.post(url,{'username':'sandeep','blog':'this is'})
		url = reverse('delete')
		assert_that(self.client.post(url,{'identity':1}).url,equal_to('/deleted'))
	
	def test_login_logout(self):
		url = reverse('login')
		assert_that(self.client.post(url,{'username':'he','password':'he'}).url,equal_to('/loggedin'))
		url = reverse('logout')	
		assert_that(self.client.post(url).url,equal_to('/loggedout'))
		