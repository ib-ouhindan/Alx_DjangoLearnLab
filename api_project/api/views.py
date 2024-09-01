from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields in the Book model
