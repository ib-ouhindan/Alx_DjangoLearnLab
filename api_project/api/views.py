from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieves all Book objects
    serializer_class = BookSerializer  # Uses the BookSerializer
