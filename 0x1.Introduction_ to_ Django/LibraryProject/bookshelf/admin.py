from django.contrib import admin

from django.contrib import admin
from .models import Book

# Customize the Book admin interface
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality on the title and author fields
    search_fields = ('title', 'author')

# Register the customized admin interface
admin.site.register(Book, BookAdmin)
