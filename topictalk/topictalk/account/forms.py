from django import forms
from django.contrib.auth.forms import UserCreationForm

from topictalk.account.models import TopicTalkUser


class TopicTalkUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = TopicTalkUser
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control', 'type': 'email'})
        }
