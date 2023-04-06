from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, default="")
    date = models.DateTimeField(default=datetime.now())

    
    def __str__(self):
        return self.title