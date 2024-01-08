from django.shortcuts import render, redirect

from topictalk.common.forms import SearchForm
from topictalk.post.models import Post, Like, Comment, LikeComment


# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_posts = all_posts.filter(choose_community__icontains=search_form.cleaned_data['community_name'])

    context = {
        'all_posts': all_posts,
        'search_form': search_form
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, post_id):
    post = Post.objects.get(id=post_id)
    liked_object = Like.objects.filter(to_post_id=post_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_post=post)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')


def like_functionality_about_comments(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    liked_comment = LikeComment.objects.filter(to_comment_id=comment_id).first()

    if liked_comment:
        liked_comment.delete()
    else:
        like = LikeComment(to_comment=comment)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{comment_id}')
