from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView
from django.http import Http404
from .models import Topic, Article
from .forms import TopicForm, AuthUserForm, RedistrUserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class MainView(View):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        articles = Article.objects.all()
        return render(request, 'mysite/index.html', context={'topics': topics, 'articles': articles})

class ArticleListView(ListView):
    paginate_by = 3
    model = Article
    template_name = 'mysite/topic.html'
    context_object_name = 'articles'

    def get_queryset(self):
        id_ = self.request.GET.get('id')
        new_context = Article.objects.filter(
            topic_id=id_,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context

class ArticleWithoutTopicListView(ListView):
    paginate_by = 3
    model = Article
    template_name = 'mysite/topic.html'
    context_object_name = 'articles'

    def get_queryset(self):
        new_context = Article.objects.filter(topic__isnull=True)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ArticleWithoutTopicListView, self).get_context_data(**kwargs)
        return context

class TopicsEditView(View):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        return render(request, 'mysite/actions/topics/topic_edit.html', context={'topics': topics})

class TopicCreateView(CreateView):
    model = Topic
    success_url = '/topics/edit'
    template_name = 'mysite/actions/topics/create.html'
    fields = ['topic']

class TopicUpdateView(UpdateView):
    model = Topic
    success_url = '/topics/edit'
    template_name = 'mysite/actions/topics/update.html'
    fields = ['topic']

class TopicDeleteView(DeleteView):
    model = Topic
    success_url = '/topics/edit'
    template_name = 'mysite/actions/topics/delete.html'
    fields = ['topic']

class ArticlesEditView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'mysite/actions/articles/article_edit.html', context={'articles': articles})

class ArticleCreateView(CreateView):
    model = Article
    success_url = '/articles/edit'
    template_name = 'mysite/actions/articles/create.html'
    fields = ['topic', 'title', 'text', 'image']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleView(DetailView):
    model = Article
    template_name = 'mysite/article.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    success_url = '/articles/edit'
    template_name = 'mysite/actions/articles/update.html'
    fields = ['topic', 'title', 'text', 'image']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/articles/edit'
    template_name = 'mysite/actions/articles/delete.html'
    fields = ['topic', 'title', 'text', 'image']

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
