from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from topictalk.account.forms import TopicTalkUserCreationForm
from topictalk.account.models import TopicTalkUser


# Create your views here.
def login(request):
    return render(request, template_name='account/sign-in.html')


class UserRegisterView(views.CreateView):
    model = TopicTalkUser
    form_class = TopicTalkUserCreationForm
    template_name = 'account/sign-up.html'
    success_url = reverse_lazy('login')


def details_profile(request, pk):
    return render(request, template_name='account/profile.html')


def edit_profile(request, pk):
    return render(request, template_name='account/edit-profile.html')


def delete_profile(request, pk):
    return render(request, template_name='account/delete-profile.html')
