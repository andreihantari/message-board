from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # Return first 50 characters of the post

# Create your models here.
