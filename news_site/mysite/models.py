from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

class Article(models.Model):
    # topic = models.CharField()
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
