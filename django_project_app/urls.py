from django.urls import path

from django_project_app.views import *

urlpatterns = [
    path("", get_hello),
    path("blog/", index_page)
]