
#### **Retrieve the Created Book**
- **Command:** Retrieve and display all attributes of the book you just created.
- **Documentation:** Create a file named `retrieve.md` and include the following:

```markdown
# Retrieve the Created Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Output: Display the attributes of the book
book.title, book.author, book.publication_year
