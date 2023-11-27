from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("signup/", views.UserCreateAPIView.as_view(), name="signup"),
]
