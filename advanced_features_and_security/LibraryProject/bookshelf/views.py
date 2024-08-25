from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'templates/relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass

# Create your views here.
