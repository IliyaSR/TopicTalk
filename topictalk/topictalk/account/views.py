from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from topictalk.account.forms import TopicTalkUserCreationForm, LoginForm, TopicTalkUserEditForm
from topictalk.account.models import TopicTalkUser
from django.contrib.auth import views as auth_views

from topictalk.post.models import Post


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
    current_profile = TopicTalkUser.objects.get(pk=pk)
    posts = Post.objects.filter(user_id=current_profile.pk)
    number_of_posts = posts.count()

    context = {
        "current_profile": current_profile,
        'number_of_posts': number_of_posts
    }

    return render(request, template_name='account/profile.html', context=context)


class UserEditView(views.UpdateView):
    model = TopicTalkUser
    form_class = TopicTalkUserEditForm
    template_name = 'account/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):
    model = TopicTalkUser
    template_name = 'account/delete-profile.html'

    def post(self, *args, pk):
        user_posts = Post.objects.filter(user_id=pk)
        user_posts.delete()
        self.request.user.delete()
        return redirect('home')