from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from topictalk.account.forms import TopicTalkUserCreationForm, LoginForm
from topictalk.account.models import TopicTalkUser
from django.contrib.auth import views as auth_views


# Create your views here.
class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'account/sign-in.html'
    next_page = reverse_lazy('home')


class UserRegisterView(views.CreateView):
    model = TopicTalkUser
    form_class = TopicTalkUserCreationForm
    template_name = 'account/sign-up.html'
    success_url = reverse_lazy('login')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


def details_profile(request, pk):
    return render(request, template_name='account/profile.html')


def edit_profile(request, pk):
    return render(request, template_name='account/edit-profile.html')


def delete_profile(request, pk):
    return render(request, template_name='account/delete-profile.html')
