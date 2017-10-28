from django.db import models

# Create your models here.

class News(models.Model):
    title = models.TextField(max_length=10000000000000)
    description = models.TextField(max_length=10000000000000000000000)
    url = models.URLField()
    date = models.CharField(max_length=255, null=True)
    url_image = models.TextField(max_length=500, null=True)
    source = models.CharField(max_length=255, null=True)
    latest_updated = models.CharField(max_length=255, null=True) #Ultima fecha en que se actualizó
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
