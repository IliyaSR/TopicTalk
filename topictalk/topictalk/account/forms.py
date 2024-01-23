from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import TextInput, PasswordInput

from topictalk.account.models import TopicTalkUser


class TopicTalkUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = TopicTalkUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(
                attrs={'id': 'floatingInput', 'class': 'form-control', 'type': 'username', 'placeholder': 'Username'}),
            'email': forms.TextInput(
                attrs={'id': 'floatingInput', 'class': 'form-control', 'type': 'email', 'placeholder': 'Username'}),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "type": 'password'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat password",
                "class": "form-control",
                "type": 'password'
            }
        )
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'floatingInput', 'class': 'form-control', 'type': 'username', 'placeholder': 'Username'
            })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "type": 'password'
            }
        )
    )


class TopicTalkUserEditForm(forms.ModelForm):
    class Meta():
        model = TopicTalkUser
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                "type": 'text', 'id': 'username'
            }),
            'email': forms.TextInput(attrs={
                'type': 'text', 'id': 'username', 'class': 'email-input'
            })
        }
