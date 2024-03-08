#from django.conf.urls import url
from django.urls import path, include
from .views import (
    AuthorListCreateView,
    AuthorRetrieveUpdateDestroyView,
    BookListCreateView,
    BookRetrieveUpdateDestroyView
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view()),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view()),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),
]