from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', LoginUserView.as_view(), name='login'),
    path('register', RedistrUserView.as_view(), name='register'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('topics/edit', TopicsEditView.as_view(), name='edit_topics'),
    path('topic/create', TopicCreateView.as_view(), name='create_topic'),
    path('<int:pk>/update', TopicUpdateView.as_view(), name='update_topic'),
    path('<int:pk>/delete', TopicDeleteView.as_view(), name='delete_topic'),
    path('articles/edit', ArticlesEditView.as_view(), name='edit_articles'),
    path('articles/create', ArticleCreateView.as_view(), name='create_article'),
    # path('<int:pk>/update', TopicUpdateView.as_view(), name='update_topic'),
    # path('<int:pk>/delete', TopicDeleteView.as_view(), name='delete_topic'),
    path('articles/<int:pk>', ArticleView.as_view(), name='article'),
]
