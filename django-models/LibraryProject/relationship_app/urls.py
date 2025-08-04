from django.urls import path
from .views import list_books, LibraryDetailView
from .views import RegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
