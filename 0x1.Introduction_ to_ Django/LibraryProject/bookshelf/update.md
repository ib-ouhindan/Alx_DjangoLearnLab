
#### **Update the Title of the Book**
- **Command:** Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
- **Documentation:** Create a file named `update.md` and include the following:

```markdown
# Update the Title of the Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Output: Display the updated title
book.title
