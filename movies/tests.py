from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Genre

class GenreTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')
        self.client.login(username='test', password='test123')

    def test_add_genre(self):
        response = self.client.post(reverse('genre_add'), {'name': 'Comedy'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Genre.objects.count(), 1)