from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Tree , Envelope

# Create your views here.

def list_of_trees(request):
    context = {}
    
    try:
        
        trees = Tree.objects.all()
        context['trees'] = [tree.get_information() for tree in trees]
    
    except Exception as e:
        pass
    
    return render(request, 'list_of_trees/index.html', context)