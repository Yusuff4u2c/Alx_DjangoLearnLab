from django.db import models

class Author(models.Model):
    """
    Author model represents a writer. 
    - name: author's full name (string)
    Relation: one Author -> many Book via Book.author ForeignKey.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book.
    Fields:
    - title: string title of the book.
    - publication_year: integer year when the book was published.
    - author: ForeignKey to Author establishing a one-to-many relationship.
    The related_name 'books' on the author allows accessing author.books.all().
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
