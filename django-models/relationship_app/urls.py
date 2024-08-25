from django.contrib import admin
from django.urls import path, include
from .views import list_books,LibraryDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]
