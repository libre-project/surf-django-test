from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Author, Book

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
    success_url = reverse_lazy('author-list')

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

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

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('author-list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('author-list')

class BookDetail(DetailView):
    model = Book

class BookList(ListView):
    model = Book