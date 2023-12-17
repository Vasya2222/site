from django.db import models

# Create your models here.


class Blog(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='blog/image')
    date = models.DateTimeField()
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title