from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.http import Http404
from .models import Topic, Article
from .forms import TopicForm, AuthUserForm, RedistrUserForm


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

class TopicUpdateView(UpdateView):
    model = Topic
    template_name = 'mysite/actions/topics/update.html'
    fields = ['topic']

class TopicDeleteView(DeleteView):
    model = Topic
    success_url = '/'
    template_name = 'mysite/actions/topics/delete.html'
    fields = ['topic']

class ArticleView(View):
    def get(self, request, slug, *args, **kwargs ):
        try:
            article = Article.objects.get(url=slug)
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'mysite/article.html', context={'article': article})

class LoginUserView(LoginView):
    template_name = 'mysite/auth/login.html'
    form_class = AuthUserForm
    success_url = '/'

    def get_success_url(self):
        return self.success_url

class RedistrUserView(CreateView):
    model = User
    template_name = 'mysite/auth/register.html'
    success_url = '/'
    form_class = RedistrUserForm

class LogoutUserView(LogoutView):
    next_page = '/'
