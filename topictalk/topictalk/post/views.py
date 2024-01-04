from django.shortcuts import render, redirect

from topictalk.post.forms import PostForm, CommentForm
from topictalk.post.models import Post, Like


# Create your views here.


def post_details(request, pk):
    current_post = Post.objects.get(pk=pk)
    comments = current_post.comment_set.all()
    context = {
        'current_post': current_post,
        'comments': comments
    }

    return render(request, template_name='post/post-details.html', context=context)


def minecraft(request):
    return render(request, template_name='post/minecraft-post.html')


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}

    return render(request, template_name='post/post-page.html', context=context)


