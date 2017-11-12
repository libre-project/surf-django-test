from django.db import models
from django.core.urlresolvers import reverse

class Author(models.Model):
    # Django сам добавляет эту строку
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name='Имя')

    class Meta:
        db_table = 'authors'
        ordering = ['name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Book(models.Model):
    # Django сам добавляет эту строку
    #id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="book",
        related_query_name="books",
        verbose_name = 'Автор')
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        db_table = 'books'
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])