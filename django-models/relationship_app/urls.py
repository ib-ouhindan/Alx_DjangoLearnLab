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
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    
]
["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
