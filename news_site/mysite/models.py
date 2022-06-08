from django.db import models

class Article(models.Model):
    # topic = models.CharField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
