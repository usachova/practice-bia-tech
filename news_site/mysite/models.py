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
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст статьи')
    image = models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='изображение')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['topic']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='комментатор')
    text = models.TextField()