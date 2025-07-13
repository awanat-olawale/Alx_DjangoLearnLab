# All CRUD Operations

### CREATE Operation

from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

### Expected Output

None displayed upon successful creation of database

### RETRIEVE Operation

from bookshelf.models import Book
book = Book.objects.get(title="1984") 
print(book.title, book.author, book.publication_year)

### Expected Output

1984 George Orwell 1949

### UPDATE Operation

from bookshelf.models import Book
book = Book.objects.get(title="1984") 
book.title = "Nineteen Eighty-Four"  
book.save()
print(book.title)

### Expected Output

Nineteen Eighty-Four

### DELETE Operation

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())

### Expected Output

(1, {'bookshelf.Book': 1})
<QuerySet []>
