from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import *

def book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, 'library/book.html', {'book': book})
