from django.shortcuts import render, redirect

from topictalk.post.forms import PostForm, CommentForm
from topictalk.post.models import Post, Like


# Create your views here.


def post_details(request, pk):
    current_post = Post.objects.get(pk=pk)
    comments = current_post.comment_set.all()
    comment_form = CommentForm()
    context = {
        'current_post': current_post,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, template_name='post/post-details.html', context=context)


def minecraft(request):
    minecraft_posts = Post.objects.filter(choose_community='Minecraft')
    context = {
        'minecraft_posts': minecraft_posts
    }

    return render(request, template_name='post/minecraft-post.html', context=context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}

    return render(request, template_name='post/post-page.html', context=context)


def like_functionality(request, post_id):
    post = Post.objects.get(id=post_id)
    liked_object = Like.objects.filter(to_post_id=post_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_post=post)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')


def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_post = post
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')
