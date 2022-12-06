from django.urls import path

from django_project_app.views import get_hello

urlpatterns = [
    path("", get_hello)
]