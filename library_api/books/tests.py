from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {
            'title': 'Test Book',
            'author': 'Author Name',
            'published_date': '2020-01-01',
            'isbn': '1234567890123',
            'pages': 300,
            'cover': 'http://example.com/cover.jpg',
            'language': 'English'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        url = reverse('book-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
