from django.contrib import admin
from django.urls import path, include
from .views import list_books,LibraryDetailView
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]

urlpatterns = [
    # URL pattern for the login view
    path('login/', CustomLoginView.as_view(), name='login'),
    
    # URL pattern for the logout view
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    # URL pattern for the registration view
    path('register/', RegisterView.as_view(), name='register'),
    
    # Add other URL patterns here if needed
]
