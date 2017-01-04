from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    fullName = models.CharField(max_length=128)
    cellphone =  models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)
    eemail = models.CharField(max_length=128) 
    
    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'

# Create your models here.
