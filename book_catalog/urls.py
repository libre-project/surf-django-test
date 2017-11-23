"""book_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .books.views import AuthorCreate, AuthorUpdate, AuthorDelete, AuthorDetail
from .books.views import BookCreate, BookUpdate, BookDelete, BookDetail, BookSearchView

urlpatterns = [
    url(r'^$', BookList.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^author/$', AuthorList.as_view(), name='author-list'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^author/new/$', AuthorCreate.as_view(), name='author-new'),
    url(r'^author/edit/(?P<pk>\d+)/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'^author/delete/(?P<pk>\d+)/$', AuthorDelete.as_view(), name='author-delete'),
    url(r'^book/$', BookList.as_view(), name='book-list'),
    url(r'^book/(?P<pk>\d+)/$', BookDetail.as_view(), name='book-detail'),
    url(r'^book/new/$', BookCreate.as_view(), name='book-new'),
    url(r'^book/edit/(?P<pk>\d+)/$', BookUpdate.as_view(), name='book-update'),
    url(r'^book/delete/(?P<pk>\d+)/$', BookDelete.as_view(), name='book-delete'),
    url(r'^search/$', BookSearchView.as_view(), name='search'),
]
