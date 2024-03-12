from django.db import models

# Create your models here.
class Actor(models.Model):
    quoter=models.CharField(max_length=225)
    
    def __str__(self):
        return self.quoter

class Quote(models.Model):
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)
    quote=models.CharField(max_length=225)
    
    def __str__(self):
        return str(self.actor)