from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

    # Basic book queries
    path('books/', views.list_books, name='list_books'),
    path('books/author/<str:author_name>/', views.books_by_author, name='books_by_author'),
    path('library-books/<int:library_id>/', views.books_in_library, name='books_in_library'),
    path('library-librarian/<int:library_id>/', views.library_librarian, name='library_librarian'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Book management with permissions
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),
]
