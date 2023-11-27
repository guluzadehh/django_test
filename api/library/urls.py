from django.urls import path
from . import views

app_name: str = "library"

urlpatterns: list = [
    path("", views.BookListCreateAPIView.as_view(), name="book-list"),
    path(
        "<int:pk>/",
        views.BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-detail",
    ),
]
