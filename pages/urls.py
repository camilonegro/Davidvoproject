from django.urls import path

from . import views

urlpatterns = [
    path("<slug>", views.page, name="page")
]