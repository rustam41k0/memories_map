from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class MemoriesViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Smith',
                            username='testuser', password='12345')

    def test_view_url_exists_for_login_user(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get('/memories/')
        self.assertEqual(responce.status_code, 200)

    def test_view_url_does_not_exists_for_no_login_user(self):
        responce = self.client.get('/memories/')
        self.assertNotEqual(responce.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memories'))
        self.assertEqual(responce.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memories'))
        self.assertEqual(responce.status_code, 200)

        self.assertTemplateUsed(responce, 'main.html')


class MemoriesCreateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Smith',
                            username='testuser', password='12345')

    def test_view_url_exists(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get('/add-memory/')
        self.assertEqual(responce.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memory_create'))
        self.assertEqual(responce.status_code, 200)

    def test_uses_correct_template(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memory_create'))
        self.assertEqual(responce.status_code, 200)

        self.assertTemplateUsed(responce, 'addmemory.html')
