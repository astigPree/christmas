from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import Tree , Envelope

# Create your views here.

class TreeListView(ListView):
    model = Tree
    template_name = 'treelistview/index.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Tree.objects.filter(is_found=True).order_by('-found_at')

    


