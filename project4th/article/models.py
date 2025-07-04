from django.db import models
from django.db.models import TextField
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms import ModelForm
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    def get_absolute_url(self):
        return reverse("detail", args={self.id})

class Comment(models.Model):
    article = models.ForeignKey(Article,related_name= "comments" , on_delete = models.CASCADE)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.writer}- {self.comment}"

    def get_absolute_url(self):
        return reverse("list")
    



    #add mixins thing from the video