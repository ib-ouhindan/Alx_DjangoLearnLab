from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author

class BookAPITests(APITestCase):
    
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter", 
            publication_year=1997, 
            author=self.author
        )self.client.login
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.books_url = reverse('book-list')

    def test_create_book(self):
        data = {
            "title": "The Hobbit",
            "publication_year": 1937,
            "author": self.author.id
        }
        response = self.client.post(self.books_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, data['title'])

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
class BookFilteringTests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Tolkien")
        self.book1 = Book.objects.create(title="The Hobbit", publication_year=1937, author=self.author)
        self.book2 = Book.objects.create(title="The Lord of the Rings", publication_year=1954, author=self.author)
        self.books_url = reverse('book-list')

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.books_url}?author__name=Tolkien")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.books_url}?search=Hobbit")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.books_url}?ordering=publication_year")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')
      class BookPermissionTests(APITestCase):
    
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter", 
            publication_year=1997, 
            author=self.author
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.id})

    def test_permission_required_for_creation(self):
        # Set permissions so only authenticated users can create
        response = self.client.post(reverse('book-list'), {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Simulate authentication and test again
        self.client.force_authenticate(user=self.author)
        response = self.client.post(reverse('book-list'), {
            "title": "The Hobbit",
            "publication_year": 1937,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
