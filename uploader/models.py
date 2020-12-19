from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='static/images')
    cv = models.FileField(upload_to='static/cvs')

    def __str__(self):
        return self.name