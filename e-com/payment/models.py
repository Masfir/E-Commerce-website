from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,  blank= True, null = True)
    first_name = models.CharField(max_length = 100, blank= True, null = True)
    last_name = models.CharField(max_length = 100, blank= True, null = True)
    country = models.CharField(max_length = 100, blank= True, null = True)
    phonenumber= models.CharField(max_length = 100, blank= True, null = True)
    email = models.CharField(max_length = 100, blank= True, null = True) 
    created = models.DateTimeField(auto_now_add =True)
    
    def __str__(self):
        return self.first_name
    
    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for fields_name in field_names:
            value = getattr(self, fields_name)
            if value is None or value =='':
                return False
            else:
                return True 
    