from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView
from django.http import Http404
from .models import Topic, Article
from .forms import TopicForm

class MainView(View):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        return render(request, 'mysite/index.html', context={'topics': topics})

class TopicView(View):
    pass

def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('ошибка')

    form = TopicForm()
    data = {
        'form': form
    }
    return render(request, 'mysite/actions/topics/create.html', data)


class ArticleView(View):
    def get(self, request, slug, *args, **kwargs ):
        try:
            article = Article.objects.get(url=slug)
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'mysite/article.html', context={'article': article})

# class ArticleUpdateView(UpdateView):
#     model = Article
#     template_name = 'update.html'