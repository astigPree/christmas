
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.list_of_trees, name='list_of_trees'),
]


