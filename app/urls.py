
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.list_of_trees, name='list_of_trees'), 
    path('visit/<str:tree_id>/', views.visit_tree, name='visit_tree'),
    path('rename/<str:tree_id>/', views.rename_tree, name='rename_tree'),
]


