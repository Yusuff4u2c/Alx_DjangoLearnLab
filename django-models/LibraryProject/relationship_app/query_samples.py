from bookshelf.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'.")
        return []


# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in library '{library.name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")
        return []


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for library '{library.name}': {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'.")
        return None


# Sample usage (can be tested in Django shell)
if __name__ == "__main__":
    get_books_by_author("John Doe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
