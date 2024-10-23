from django.db import models

# Create your models here.

class Tree(models.Model):
    
    name = models.CharField(max_length=225 , default='', blank=True, null=True)
    tree_id = models.CharField(max_length=255, blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image_index = models.SmallIntegerField(null=True, blank=True) # Index of the image to use
    level = models.IntegerField(default=0, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    found_at = models.DateTimeField( default=None ,null=True, blank=True)
    is_found = models.BooleanField(default=False, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.name} - {self.location}"
    
    def get_information(self):
        return {
            'name': self.name,
            'tree_id': self.tree_id,
            'location': self.location,
            'image_index': self.image_index,
            'location_name': self.location_name,
            'level' : self.level,
            'created_at': self.created_at,
            'found_at' : self.found_at,
        }
    
    def get_number_of_envelope(self):
        envelope_count = Envelope.objects.filter(tree_id=self.tree_id).count()
        return envelope_count
    
    def get_all_envelope(self):
        envelopes = Envelope.objects.filter(tree_id=self.tree_id)
        return {
            'envelopes' : [
                envelope.get_information() for envelope in envelopes
            ]
        }


class Envelope(models.Model):
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(max_length=255, blank=True, null=True)
    tree_id = models.CharField(max_length=255, blank=True, null=True)
    image_index = models.SmallIntegerField(null=True, blank=True) # Index of the image to use
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.owner_name} - {self.tree_id}"
    
    def get_information(self):
        return {
            'owner_name' : self.owner_name,
            'content' : self.content,
            'image_index': self.image_index,
            'created_at' : self.created_at 
        }


