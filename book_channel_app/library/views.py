from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .models import *

def book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    category = []
    links_order = {}
    if book:
        category = book.category_ids.all()
        
        links = Link.objects.filter(book_id=book.id).order_by('format')
        links_order ={u[0].upper(): [] for u in Link.objects.filter(book_id=book.id).values_list('format')}

        for link in links:
            links_order[link.format.upper()].append(link)

    return render(request, 'library/book.html', {
        'book': book, 
        'categories': category,
        'links': links_order,
        })


class HomePageView(ListView):
    # paginate_by = 2
    template_name = "library/home.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Book.objects.all().order_by('-publish_date')
