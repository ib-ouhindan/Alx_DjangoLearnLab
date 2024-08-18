
#### **Delete the Book Instance**
- **Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.
- **Documentation:** Create a file named `delete.md` and include the following:

```markdown
# Delete the Book Instance

```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Output: Check if the book was deleted
Book.objects.all()
