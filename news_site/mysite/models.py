from django.contrib.auth.models import User
from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return '/'

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, verbose_name='тема', blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
