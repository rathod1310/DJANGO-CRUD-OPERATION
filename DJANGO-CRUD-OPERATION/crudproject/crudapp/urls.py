from django.urls import path
from . import views

urlpatterns = [

    # show book
    path('', views.book_list, name='book_list'),

    #add book
    path('upload/', views.upload_book, name='upload_book'),

    #read book details
    path('<int:pk>/', views.book_detail, name='book_detail'),

    #edit book details
    path('edit/<int:pk>/', views.edit_book_details, name='edit_book_details'),

    #delete book
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
