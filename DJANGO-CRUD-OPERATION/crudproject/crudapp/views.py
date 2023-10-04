from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

#show list of book
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

#add book
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})

#read book details
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_details.html', {'book': book})

#edit book details
def edit_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book_details.html', {'form': form, 'book': book})

#delete book
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})