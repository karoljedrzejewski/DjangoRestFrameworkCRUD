from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default = 'null')
    description = models.TextField()
    popularPlaces = models.TextField()
    image = models.ImageField(upload_to='images/')





    def __str__(self):
        return self.name