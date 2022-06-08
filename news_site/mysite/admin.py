from django.contrib import admin
from .models import Topic, Article

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)