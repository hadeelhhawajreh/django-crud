from django.test import TestCase,SimpleTestCase
# Create your tests here.
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import ModelBlog

# Create your tests here.

class CRUDTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'hadeel',
            email = 'hadeel@gmail.com',
            password = '123456'
        )
        self.ModelBlog = ModelBlog.objects.create(
            title = 'Book',
            author = self.user,
            body= 'body ',
        )

    def test_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_details_status(self):
        response = self.client.get(reverse('details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_details_content(self):
        response = self.client.get(reverse('details', args='1'))
        self.assertContains(response, 'Book')

    def test_update(self):
        response = self.client.post(reverse('update_blog', args='1'), {
            'author': 'hadeel',
        })
        self.assertContains(response, 'hadeel')
        self.assertNotContains(response, 'admin')
