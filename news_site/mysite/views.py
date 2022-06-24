from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin
from .models import Topic, Article, Comment
from .forms import AuthUserForm, RedistrUserForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .templatetags.auth_extras import has_group


class MainView(View):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        if search_query:
            object_list = Article.objects.filter(title__icontains=search_query)
        else:
            object_list = Article.objects.order_by('topic')
        paginator = Paginator(object_list, 5)
        page = request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            article_list = paginator.page(1)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)

        return render(request, 'mysite/index.html', {'page': page, 'article_list': article_list})

class ArticleListView(ListView):
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
    success_url = '/'
    template_name = 'mysite/actions/articles/create.html'
    fields = ['topic', 'title', 'text', 'image']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleView(FormMixin, DetailView):
    model = Article
    template_name = 'mysite/article.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self):
        article_id = self.object.article.id
        return reverse_lazy('article', kwargs={'pk': article_id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'mysite/actions/articles/update.html'
    fields = ['topic', 'title', 'text', 'image']

    def get_success_url(self):
        article_id = self.object.id
        return reverse_lazy('article', kwargs={'pk': article_id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author and not has_group(self.request.user, "admins"):
            return self.handle_no_permission()
        return kwargs

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/'
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

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'mysite/actions/comments/update.html'
    fields = ['text']

    def get_success_url(self):
        article_id = self.object.article.id
        return reverse_lazy('article', kwargs={'pk': article_id})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'mysite/actions/comments/delete.html'

    def get_success_url(self):
        article_id = self.object.article.id
        return reverse_lazy('article', kwargs={'pk': article_id})
