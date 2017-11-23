from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Author, Book

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']
    success_url = reverse_lazy('author-list')

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(LoginRequiredMixin, DeleteView):
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

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author']

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('book-list')

class BookDelete(LoginRequiredMixin, DeleteView):
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
    def get_queryset(self):
        result = super(BookSearchView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        return result
