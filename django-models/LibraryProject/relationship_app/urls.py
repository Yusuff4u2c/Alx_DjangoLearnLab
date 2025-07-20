from django.urls import path
from . import views


urlpatterns = [
    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

    # Book queries
    path('books/', views.list_books, name='list_books'),
    path('books/author/<str:author_name>/', views.books_by_author, name='books_by_author'),
    path('library-books/<int:library_id>/', views.books_in_library, name='books_in_library'),
    path('library-librarian/<int:library_id>/', views.library_librarian, name='library_librarian'),

    # Role-based access control
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Book CRUD operations with permissions
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
