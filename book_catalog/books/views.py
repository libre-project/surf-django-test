from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Author, Book
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
    success_url = reverse_lazy('author-list')

@method_decorator(login_required, name='dispatch')
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

@method_decorator(login_required, name='dispatch')
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

class AuthorDetail(DetailView):
    model = Author
    fields = ['name']
    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(author=self.object)
        return context

class AuthorList(ListView):
    model = Author
    context_object_name = 'authors_list'

class AuthorSearchView(ListView):
    model = Author
    def get_queryset(self):
        result = super(AuthorSearchView, self).get_queryset()
        name = self.request.GET.get('q')
        if name:
            result = result.filter(author__icontains = name)
        return result

@method_decorator(login_required, name='dispatch')
class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']

@method_decorator(login_required, name='dispatch')
class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('book-list')

@method_decorator(login_required, name='dispatch')
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

class BookDetail(DetailView):
    model = Book

class BookList(ListView):
    model = Book
    context_object_name = 'books_list'

class BookSearchView(ListView):
    model = Book
    context_object_name = 'books_list'
    # template_name = 'search_form.html'
    def get_queryset(self):
        result = super(BookSearchView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(Q(title__icontains = query) | Q(author__name__icontains = query))
        return result