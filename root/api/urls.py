from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteAPIView.as_view(), name='book-detail'),
]
