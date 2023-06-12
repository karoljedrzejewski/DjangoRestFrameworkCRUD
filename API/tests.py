from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(name='Test name', country='Test country', description='Test description')

    def test_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)


class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')

    def test_register(self):
        response = self.client.post('/auth/register/', {'username': 'testuser2', 'email': 'test2@test.com', 'password': 'testpassword2'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/auth/login/', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, 200)
