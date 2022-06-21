from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RedistrUserView.as_view(), name='register'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('topic/', ArticleListView.as_view(), name='topic'),
    path('topic/without_topic', ArticleWithoutTopicListView.as_view(), name='without_topic'),
    path('topics/edit', TopicsEditView.as_view(), name='edit_topics'),
    path('topic/create', TopicCreateView.as_view(), name='create_topic'),
    path('topic/<int:pk>/update', TopicUpdateView.as_view(), name='update_topic'),
    path('topic/<int:pk>/delete', TopicDeleteView.as_view(), name='delete_topic'),
    path('articles/edit', ArticlesEditView.as_view(), name='edit_articles'),
    path('articles/create', ArticleCreateView.as_view(), name='create_article'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='update_article'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='delete_article'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)