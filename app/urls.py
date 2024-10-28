

from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.list_of_trees, name='list_of_trees'),
]


