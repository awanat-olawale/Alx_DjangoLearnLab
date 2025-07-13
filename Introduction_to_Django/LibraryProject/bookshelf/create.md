# Create Operation

from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected Output

None displayed upon successful creation of database