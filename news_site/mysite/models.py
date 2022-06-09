from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

class Article(models.Model):
    # topic = models.CharField()
    url = models.SlugField(unique=True, default="dafault_url")
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
