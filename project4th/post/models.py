from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    seller = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"