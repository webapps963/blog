from django.db import models

# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    paper = models.CharField(max_length=128)
    page = models.CharField(max_length=128)
    way = models.CharField(max_length=128)    
    content = models.TextField()

    
    
    def __str__(self):
        return self.title