from django.contrib import admin
from .models import Tree, Envelope, TemporaryUser

# Register your models here.

admin.site.register(Tree)
admin.site.register(Envelope)
admin.site.register(TemporaryUser)
