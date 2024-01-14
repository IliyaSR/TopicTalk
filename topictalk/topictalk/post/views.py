from django.shortcuts import render, redirect

from topictalk.common.forms import SearchForm
from topictalk.post.forms import PostForm, CommentForm
from topictalk.post.models import Post, Like, Comment, LikeComment


# Create your views here.


def post_details(request, pk):
    current_post = Post.objects.get(pk=pk)
    comments = current_post.comment_set.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    context = {
        'current_post': current_post,
        'comments': comments,
        'comment_form': comment_form,
        'search_form' : search_form,
    }

    return render(request, template_name='post/post-details.html', context=context)


def minecraft(request):
    minecraft_posts = Post.objects.filter(choose_community='Minecraft')
    search_form = SearchForm()

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            minecraft_posts = minecraft_posts.filter(
                choose_community__icontains=search_form.cleaned_data['community_name'])

    context = {
        'minecraft_posts': minecraft_posts,
        'search_form': search_form
    }

    return render(request, template_name='post/minecraft-post.html', context=context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    search_form = SearchForm()
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
        'search_form': search_form
    }

    return render(request, template_name='post/post-page.html', context=context)


def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_post = post
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')


def league_of_legends(request):
    league_of_legends_posts = Post.objects.filter(choose_community='League of Legends')
    search_form = SearchForm()
    context = {
        'league_of_legends_posts': league_of_legends_posts,
        'search_form' : search_form
    }

    return render(request, template_name='post/league-of-legends.html', context=context)


def nba(request):
    nba_posts = Post.objects.filter(choose_community='NBA')
    search_form = SearchForm()
    context = {
        'nba_posts': nba_posts,
        'search_form' : search_form
    }

    return render(request, template_name='post/NBA.html', context=context)


def premier_league(request):
    premier_league_posts = Post.objects.filter(choose_community='Premier League')
    search_form = SearchForm()
    context = {
        'premier_league_posts': premier_league_posts,
        'search_form': search_form
    }

    return render(request, template_name='post/premier_league.html', context=context)


def bitecoin(request):
    bitecoin_posts = Post.objects.filter(choose_community='Bitecoin')
    search_form = SearchForm()
    context = {
        'bitecoin_posts': bitecoin_posts,
        'search_form' : search_form
    }

    return render(request, template_name='post/bitecoin.html', context=context)


def litecoin(request):
    litecoin_posts = Post.objects.filter(choose_community='Litecoin')
    search_form = SearchForm()
    context = {
        'litecoin_posts': litecoin_posts,
        'search_form' : search_form
    }

    return render(request, template_name='post/litecoin.html', context=context)


def delete_post(request, post_id):
    current_post = Post.objects.get(pk=post_id)
    current_post.delete()
    return redirect('home')


def delete_comment(request, comment_id, post_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('post-details', pk=post_id)
