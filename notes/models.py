from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    description = models.TextField()
    color = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    isFavorite = models.BooleanField(default=False)
    isTrash = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user} - {self.title}'