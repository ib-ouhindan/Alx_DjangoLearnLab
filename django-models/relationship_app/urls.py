from django.contrib import admin
from django.urls import path, include
from .views import list_books,LibraryDetailView
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView
from django.urls import path
from .views import admin_view, librarian_view, member_vie
from .views import admin_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    
]

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
