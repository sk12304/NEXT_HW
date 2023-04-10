from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()

    def deadline(self):
        d_day = self.date - timezone.now()
        return d_day.days


    def __str__(self):
        return self.title
