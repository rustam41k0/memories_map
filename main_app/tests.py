from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from main_app.models import Memory
from django.contrib.gis.geos import Point


class MemoriesViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(self.user)
        self.place = Memory.objects.create(title='Test title', description='Content test',
                                           author=self.user, location=Point(60, 60))
        self.place_data = {
            'author': self.user,
            'title': 'Beautifup place',
            'description': 'Wow, this was amazing!',
            'location': Point(60, 60)
        }

    def test_main_page_authenticated(self):
        response = self.client.get(reverse('memories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memories.html')

    def test_login_page_authenticated(self):
        response = self.client.get(reverse('sign_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_add_memory_page_authenticated(self):
        response = self.client.get(reverse('memory_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addmemory.html')

    def test_add_memory_authenticated(self):
        response = self.client.post(reverse('memory_create'), data=self.place_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Memory.objects.values()), 1)
        self.assertTemplateUsed(response, 'addmemory.html')

    def test_main_page_no_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('memories'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/sign-in/?next=/memories/')

    def test_login_page_no_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('sign_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_add_memory_page_no_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('memory_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/sign-in/?next=/add-memory/')

    def test_add_memory_no_authenticated(self):
        self.client.logout()
        response = self.client.post(reverse('memory_create'), data=self.place_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/sign-in/?next=/add-memory/')
