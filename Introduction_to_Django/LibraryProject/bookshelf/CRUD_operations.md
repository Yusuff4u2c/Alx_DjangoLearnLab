# Django Shell CRUD Operations

This document demonstrates performing Create, Retrieve, Update, and Delete operations using the Django shell for the `Book` model.

---

## CREATE

### Command:

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Output:

```python
# A Book object is created successfully
book.id
# Output: 1
```

**Book instance created successfully**.

---

## RETRIEVE

### Command:

```python
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
```

### Output:

```python
1984 George Orwell 1949
```

**Book details retrieved correctly**.

---

## UPDATE

### Command:

```python
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

### Output:

```python
Nineteen Eighty-Four
```

**Book title updated successfully**.

---

## DELETE

### Command:

```python
book.delete()
Book.objects.all()
```

### Output:

```python
<QuerySet []>
```

**Book deleted — no records remain**.
