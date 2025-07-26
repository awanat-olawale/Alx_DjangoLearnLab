# Delete Operation

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())

# Expected Output

(1, {'bookshelf.Book': 1})
<QuerySet []>
