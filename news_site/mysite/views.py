from django.shortcuts import render
from django.views import View
from .models import Topic, Article

class MainView(View):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        return render(request, 'mysite/index.html', context={'topics': topics})
