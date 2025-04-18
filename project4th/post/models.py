from django.db import models
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    seller = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    def get_absolute_url(self):
        return reverse("post_detailview", kwargs={"pk":self.pk})
    
    #it must redirect into detailview.html
    #explain again why pk instead of id