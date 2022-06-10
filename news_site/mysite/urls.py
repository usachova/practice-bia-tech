from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', NewsSiteLoginView.as_view(), name='login'),
    path('<slug>', ArticleView.as_view(), name='article'),
    path('topic/create', create_topic, name='create'),
    path('<int:pk>/update', TopicUpdateView.as_view(), name='update_topic'),
    path('<int:pk>/delete', TopicDeleteView.as_view(), name='delete_topic'),
]
