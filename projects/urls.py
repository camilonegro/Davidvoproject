from django.urls import path

from . import views

urlpatterns = [
    path('project/<slug>', views.project, name='project'),
    path('', views.home, name="home")
]