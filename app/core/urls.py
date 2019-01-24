from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('books/', book_list, name='book_list'),
    path('books/upload/', upload_book, name='upload_book'),

    path('class/books/', BookListView.as_view(), name='class_book_list'),
    path('class/books/upload', UploadBookView.as_view(), name='class_upload_book')
]
