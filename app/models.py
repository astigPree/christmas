from django.db import models

from django.utils import timezone


from . import models_utils

# Create your models here.


class TemporaryUser(models.Model):
    user_id = models.CharField(max_length=255, blank=True, null=True)
    expires_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user_id} - {self.expires_at}"
    
    def remove_if_expired(self):
        if self.expires_at < timezone.now():
            self.delete()
            

class Tree(models.Model):
    
    name = models.CharField(max_length=225 , default='', blank=True, null=True)
    tree_id = models.CharField(max_length=255, blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True)
    location = models.JSONField(blank=True, null=True, default=dict)
    """
        {
            "latitude": 12.375345854355354, 
            "longitude": 123.63267251258442
        }
    """
    image_index = models.SmallIntegerField(null=True, blank=True) # Index of the image to use
    level = models.IntegerField(default=0, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    found_at = models.DateTimeField( default=None ,null=True, blank=True)
    is_found = models.BooleanField(default=False, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.name if self.name else '[ Hidden ]'} - {self.image_index} - {self.location_name} - {self.location}"
    
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
    
    
    def get_not_found_information(self):
        return {
            'name': self.name,
            'tree_id': self.tree_id, 
            'image_index': self.image_index, 
            'level' : self.level,
            'created_at': self.created_at,
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
        
    def get_distance_of_user(self, lat, long):
        return models_utils.haversine(self.location['latitude'], self.location['longitude'], lat, long)
    
    def is_user_in_range(self, lat, long):
        return models_utils.is_within_15_meters(self.location['latitude'], self.location['longitude'], lat, long)
    
    


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


