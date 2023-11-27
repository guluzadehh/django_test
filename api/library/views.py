from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer


class BookAPIViewMixin:
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListCreateAPIView(BookAPIViewMixin, ListCreateAPIView):
    pass


class BookRetrieveUpdateDestroyAPIView(BookAPIViewMixin, RetrieveUpdateDestroyAPIView):
    pass
