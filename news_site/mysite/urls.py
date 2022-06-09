from django.urls import path
from .views import MainView, ArticleView, TopicView, create_topic

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('<slug>', ArticleView.as_view(), name='article'),
    path('topic/create', create_topic, name='create')
]
