from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# Alias user_register as register to match "views.register"
register = views.user_register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # other views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
      path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),
]
