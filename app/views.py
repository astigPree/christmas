from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.utils import timezone

from .models import Tree , Envelope, TemporaryUser

from uuid import uuid4

# Create your views here.

def list_of_trees(request):
    context = {
        'has_error' : False
    }
    
    try:
        
        found_trees = Tree.objects.filter(is_found=True).order_by('-found_at')
        not_found_trees = Tree.objects.filter(is_found=False).order_by('-created_at')
        
        if request.session.get('user_id', None):
            user = TemporaryUser.objects.create(
                user_id=str(uuid4()),
                expires_at=timezone.now() + timezone.timedelta(days=1)    
            )
            user.save()
            request.session['user_id'] = user.user_id
        
        context = {
            'found_trees' : [tree.get_information() for tree in found_trees],
            'not_found_trees' : [tree.get_not_found_information() for tree in not_found_trees]
        }
        
    
    except Exception as e:
        print(f"[] Error : {e}[]")
        context['has_error'] = True
    
    return render(request, 'list_of_trees/index.html', context)












