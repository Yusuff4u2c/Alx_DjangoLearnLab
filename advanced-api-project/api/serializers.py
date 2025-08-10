from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model.
    - Serializes all Book fields: id, title, publication_year, author.
    - Includes validation to ensure publication_year is not in the future.
      This is implemented in validate_publication_year which runs automatically
      during serializer.is_valid().
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure that the publication year is not in the future relative to the current year.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and nests related books.
    - name: the author's name.
    - books: nested representation of Book objects related to this Author.
      Uses BookSerializer with many=True and read_only=True so that books
      are displayed but not created directly via the Author serializer.
      The relationship is resolved via the Book.author ForeignKey and
      the 'related_name' on that field (author.books).
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
