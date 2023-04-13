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
    
class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()

    def __str__(self):
        return self.content
    
    
class Recomment(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    content=models.TextField()

    def __str__(self):
        return self.content