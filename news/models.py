from django.db import models

# Create your models here.

class News(models.Model):
    title = models.TextField(max_length=10000000000000)
    description = models.TextField(max_length=10000000000000000000000)
    url = models.URLField()
    date = models.CharField(max_length=255)
    url_image = models.TextField(max_length=500)
    source = models.CharField(max_length=255)
    latest_updated = models.CharField(max_length=255) #Ultima fecha en que se actualizó
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
