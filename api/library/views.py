from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer


class BookAPIViewMixin:
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListCreateAPIView(BookAPIViewMixin, ListCreateAPIView):
    filter_backends = [OrderingFilter]
    ordering_fields = ["name"]


class BookRetrieveUpdateDestroyAPIView(BookAPIViewMixin, RetrieveUpdateDestroyAPIView):
    pass
