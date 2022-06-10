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

class RedistrUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
