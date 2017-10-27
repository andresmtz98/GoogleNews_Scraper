from django.db import models

# Create your models here.

class News(models.Model):
    title = models.TextField(max_length=10000000000000)
    description = models.TextField(max_length=10000000000000000000000)
    url = models.URLField()
    date = models.CharField(max_length=255)
    image_url = models.CharField(max_length=500)
    source = models.CharField(max_length=255)
    last_updated = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)