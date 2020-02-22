from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = " books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        # return Book.objects.filter(#hardcoding values
        #     Q(title__icontains="gravity") | Q(title__icontains="vegan recipes")
        # )

    # queryset = Book.objects.filter(title__icontains="Gravity")
