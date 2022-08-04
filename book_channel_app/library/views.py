from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import *

def book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    category = []
    links_order = {}
    if book:
        category = book.category_ids.all()
        
        links = Link.objects.filter(book_id=book.id).order_by('format')
        links_order ={u[0]: [] for u in Link.objects.filter(book_id=book.id).values_list('format')}

        for link in links:
            links_order[link.format].append(link)

    return render(request, 'library/book.html', {
        'book': book, 
        'categories': category,
        'links': links_order,
        })
