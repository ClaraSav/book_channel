import json

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.core.paginator import Paginator


from .models import *
from .forms import *


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

def search_books(request):
    books = {'title': 'libro1'}

    return HttpResponse(json.dumps(books), content_type='application/json')


class HomePageView(ListView):
    paginate_by = 10
    template_name = "library/home.html"
    model = Book
    form_class = BooksSearchForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        paginator = Paginator(Book.objects.all().order_by('-publish_date'), self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {
            'form': form,
            'page_obj': page_obj
            })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['categories'] or Category.objects.all()
            books_search = Book.objects.filter(title__icontains=form.cleaned_data['name'], 
                                               category_ids__in=categories).distinct().order_by('-publish_date')

            paginator = Paginator(books_search, self.paginate_by)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, self.template_name, {
                'form': form,
                'page_obj': page_obj
                })

        paginator = Paginator(Book.objects.all().order_by('-publish_date'), self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {
            'form': form,
            'page_obj': page_obj
            })
