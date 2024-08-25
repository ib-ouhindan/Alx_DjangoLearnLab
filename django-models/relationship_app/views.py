from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

def list_books(request):
    books = Book.objects.all()
    return render(request, 'templates/relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/relationship_app/library_detail.html'
    context_object_name = 'library'


# Login view
class CustomLoginView(LoginView):
    template_name = 'templates/relationship_app/login.html'

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'templates/relationship_app/logout.html'

# Registration view
class RegisterView(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
