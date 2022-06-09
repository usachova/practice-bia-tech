from .models import Article, Topic
from django.forms import ModelForm

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']