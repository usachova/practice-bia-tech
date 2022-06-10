from django.contrib.auth.forms import AuthenticationForm

from .models import Article, Topic
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']

class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
